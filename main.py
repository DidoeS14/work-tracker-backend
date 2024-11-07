import datetime
import os
import time

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from config import admin
from csv_handler import logger

app = Flask(__name__, static_folder='dist')
CORS(app)  # Enable Cross-Origin Resource Sharing


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path=''):
    if path != '' and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/admin-auth", methods=["POST"])
def adminAuth():
    """
    Checks if the uid of the given user matches with the admin uid
    :return: JSON and HTTP Status
    """
    uid = request.get_json()
    if uid == admin:
        return jsonify({"admin":True}), 200

    return jsonify({"admin":False}), 200


@app.route("/stop-timer", methods=["POST"])
def writeData():
    """
    Writes the data inside a .csv log file using the logger object from CSVLogger
    :return: JSON and HTTP Status
    """
    user = request.get_json().get("email")
    time = request.get_json().get("time")
    report = request.get_json().get("report")
    date = datetime.datetime.now().date()
    print(f'Data: {date} | {user} | {time} | {report} |')
    logger.write_data(user, time, report)

    return jsonify(None), 200


@app.route("/csv-user", methods=["POST"])
def sendUserData():
    """
    Sends the log with all worked hours and daily reports to the user that is requesting that
    :return: JSON and HTTP Status
    """
    try:
        # Ensure the body is parsed as JSON
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON or empty body"}), 400

        # Try to get the email from the parsed JSON
        email = data.get("email")

        print(f"Received email: {email}")
        logger.refresh()
        userData = logger.get_user_data(email)
        return jsonify({"message": "Data received successfully", "userData":userData}), 200

    except Exception as e:
        # Catch any unexpected errors and return a helpful message
        print(e)
        return jsonify({"error": "Unexpercted error!"}), 500

@app.route("/csv-users",methods=["GET"])
def sendAllUsersData():
    """
    Sends back the log data of all regular users to the client
    :return: JSON and HTTP Status
    """
    try:
        logger.refresh()
        data = logger.get_all_data()
        return jsonify({"message": "Data received successfully", "userData": data}), 200
    except Exception as e:
        print(e)
        return jsonify({"error":"Unexpected error!"}),500


if __name__ == '__main__':
    app.run(debug=True) # default host is http://127.0.0.1:5000

from flask import Flask, jsonify, request
from flask_cors import CORS

from users import checkExist, checkAdmin


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return '<p>heloo</p>'
@app.route("/test")
def test():
    print('test call')
    return jsonify(message="This is the response from /test")  # Return a JSON response

@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    exists = checkExist(username,password)

    if not exists:
        return jsonify({'error':'User does not exist!'})

    isAdmin = checkAdmin(username)

    if isAdmin:
        response_data = {"user_exists": exists, "is_admin": isAdmin, 'push':''}

    print(f'User exists: {exists}; User is admin: {isAdmin}')

    response_data = {"user_exists": exists, "is_admin": isAdmin}
    print(f"Returning response: {response_data}")  # Debugging line

    return jsonify(response_data), 200



if __name__ == '__main__':
    app.run()

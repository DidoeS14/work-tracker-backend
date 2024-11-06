import json

try:
    # Load the JSON data from the file
    with open('users.json', 'r') as f:
        users_data = json.load(f)
        print(users_data)

    # Check the 'users' structure and access individual users
    if 'users' in users_data:
        for user in users_data['users']:
            print(f"Name: {user['name']}")
            print(f"Password: {user['password']}")
            print(f"Admin: {user['admin']}")
            print()  # Print a blank line between users
    else:
        print("Users structure not followed!")
        print('Example:')
        print("""{
  "users": [
    {
      "name": "admin",
      "password": "admin",
      "admin": "true"
    },
  ]
}""")
except FileNotFoundError:
    print('No users.json file found!')
except json.JSONDecodeError:
    print('Error decoding JSON data!')

def checkExist(username,password):
    for user in users_data['users']:
        if username == user['name'] and password == user['password']:
            return True
    return False

def checkAdmin(username):
    for user in users_data['users']:
        if username == user['name'] and user['admin'] == 'true':
            return True
    return False


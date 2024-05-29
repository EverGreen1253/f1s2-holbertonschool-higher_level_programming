#!/usr/bin/python3
""" Nameless Module for Task 5 """

import time
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager, get_jwt

app = Flask(__name__)
auth = HTTPBasicAuth()

# Step 1 - User and Password pairs
users = {
    "john": generate_password_hash("1234"),
    "jane": generate_password_hash("5678"),
    "bill": generate_password_hash("1357"),
    "dave": generate_password_hash("2468")
}

roles = {
    "admin": ["john"],
    "user": ["jane", "bill", "dave"]
}

# Step 2 - Setting up the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "i-love-fish-and-chips"
jwt = JWTManager(app)

@auth.verify_password
def verify_password(username, password):
    """ Verify user password """
    if username in users and check_password_hash(users[username], password):
        return username
    else:
        return None

@app.route("/")
def home():
    """ Prints welcome string """
    return "Welcome to the Flask API!"

# Step 1 & 2 combined - logging in gives a JWT in return
@app.route("/login")
@auth.login_required
def login():
    """ Prints authenticated user welcome string """
    jwt_role = ""
    for key, data in roles.items():
        if auth.current_user() in data:
            jwt_role = key

    print(jwt_role)
    additional_claims = {"role": jwt_role, "created_at": time.time()}
    access_token = create_access_token(
        identity=auth.current_user(),
        additional_claims=additional_claims
    )
    return " Hello, {0}! Welcome to the Admin area!\n To test your JWT, use the following command:\n curl -H \"Authorization: Bearer {1}\" localhost:5000/jwt-admin".format(
        auth.current_user(),
        access_token
    )

@app.route("/members")
@auth.login_required
def members():
    """ Only logged in users can come here """
    return "Welcome to the Members area, {}!".format(auth.current_user())

# Step 3 - header needs to include the web token previously returned.
# Test using cURL - curl -H "Authorization: Bearer <Token goes here>" localhost:5000/jwt-admin
@app.route("/jwt-admin")
@jwt_required(optional=True)
def protected():
    """ Print welcome message to authenticated users with a JWT """
    user = get_jwt_identity()
    if user is None:
        return("401 - Unauthorized access", 401)

    claims = get_jwt()

    allowed_users = roles['admin']
    if user not in allowed_users:
        return " You're not supposed to be here!\n Only those with the 'admin' role can come here!\n"

    return " Welcome to the JWT area, {0}!\n Your role is {1}.\n The token was created at {2}\n".format(user, claims['role'], claims['created_at'])


# Set debug=True for the server to auto-reload when there are changes
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)

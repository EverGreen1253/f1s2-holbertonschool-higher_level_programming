#!/usr/bin/python3
""" Nameless Module for Task 5 """

from flask import Flask, jsonify, request, abort
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "i-love-anime-and-video-games"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": "1234", "role": "user"},
    "admin1": {"username": "admin1", "password": "4321", "role": "admin"}
}

@app.route("/")
def home():
    """ Prints welcome string """
    return "Welcome to the Flask API!"

@app.route("/login", methods=["POST"])
def login():
    """ login """
    # -- Usage example --
    # curl -X POST localhost:5000/login /
    #  -H "Content-Type: application/json" /
    #  -d '{"username":"user1","password":"1234"}'

    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()

    for k in ["username", "password"]:
        if k not in data:
            abort(400, "Missing attribute {}.".format(k))

    if data["username"] not in users or data["password"] != users[data["username"]]["password"]:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=data["username"])
    return jsonify(access_token=access_token)

@app.route("/basic-protected", methods=["GET"])
@jwt_required()
def basic_protected():
    """ basic protected """
    current_user = get_jwt_identity()

    if current_user not in users:
        return jsonify({"error": "Unauthorized"}), 401

    return "Basic Auth: Access Granted\n"
    # return jsonify(logged_in_as=current_user), 200

@app.route("/jwt-protected")
@jwt_required(optional=True)
def jwt_protected():
    """ Tests whether a valid jwt is in header """
    current_identity = get_jwt_identity()
    if not current_identity:
        return jsonify({"error": "Unauthorized"}), 401

    return "JWT Auth: Access Granted\n"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """ Only for admin role users """
    current_user = get_jwt_identity()

    if current_user not in users or users[current_user]["role"] != "admin":
        return jsonify({"error": "Forbidden"}), 403

    return "Admin Access: Granted\n"


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)

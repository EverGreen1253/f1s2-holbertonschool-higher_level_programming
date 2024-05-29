#!/usr/bin/python3
""" Nameless Module for Task 4 """

from flask import Flask, jsonify, request, abort

# Step 1
app = Flask(__name__)

users = {}

@app.route("/")
def home():
    """ Prints welcome string """
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    """ Returns JSON data """
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """ Prints OK """
    return "OK"

@app.route("/info")
def info():
    """ Returns info JSON """
    i: dict = {
        "version": "1.0",
        "description": "A beginner-friendly Flask API"
    }
    return jsonify(i)

@app.route("/users/<username>")
def users_specific(username):
    """ Get specified """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """ adds a new user to the dict """
    # can_add_list = ["username", "name", "age", "city"]

    if request.get_json() is None:
        abort(400, "Not a JSON")

    req_data = request.get_json()

    if "username" not in req_data:
        return jsonify({"error": "Username is required"}), 400

    users[req_data["username"]] = {
        "name": req_data["name"],
        "age": req_data["age"],
        "city": req_data["city"]
    }
    return jsonify({"message": "User added", "user": req_data}), 201

# Set debug=True for the server to auto-reload when there are changes
if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)

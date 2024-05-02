#!/usr/bin/python3
""" Nameless Module for Task 4 """

from flask import Flask, jsonify

# Step 1
app = Flask(__name__)

# Step 2
@app.route("/")
def home():
    """ Prints welcome string """
    return "Welcome to the Flask API!"

# Step 3
@app.route("/data")
def data():
    """ Returns JSON data """
    d: dict = {
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
    return jsonify(d)

# Step 4
@app.route("/info")
def info():
    """ Returns info JSON """
    i: dict = {
        "version": "1.0",
        "description": "A beginner-friendly Flask API"
    }
    return jsonify(i)

@app.route("/users/<name>")
def users(name):
    """ Prints personalised welcome message """
    return "Hello, {}! Welcome to the Flask API!".format(name)

# Set debug=True for the server to auto-reload when there are changes
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)

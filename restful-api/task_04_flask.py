#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

dictionary = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
        },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
        }}

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def datapage():
    return jsonify([index['username'] for index in dictionary.values()])


@app.route("/status")
def statuspage():
    return "OK"


@app.route("/users/<user>")
def userpage(user):
    if user in dictionary:
        return jsonify(dictionary[user])
    else:
        return jsonify({"error": "User not found"})


@app.route("/add_user", methods=['POST'])
def adduser():
    newuser = request.get_json()
    if "username" in newuser:
        dictionary[newuser["username"]] = newuser
        return jsonify({"message": "User addded", "user": newuser}), 201
    else:
        return jsonify({"error": "Username is required"}), 400


if __name__ == "__main__":
    app.run()

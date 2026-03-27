#!/usr/bin/env python3
"""
Simple Flask API
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    """
    Root endpoint
    """
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_data():
    """
    Return a list of all usernames
    """
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """
    Return API status
    """
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Return full user object by username
    """
    user = users.get(username)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user to the users dictionary
    """
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()

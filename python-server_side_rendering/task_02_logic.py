#!/usr/bin/python3
"""Flask app that renders dynamic content using Jinja."""

import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/items")
def items():
    """Render items from a JSON file."""
    with open("items.json", "r") as file:
        data = json.load(file)

    items_list = data.get("items", [])

    return render_template("items.html", items=items_list)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

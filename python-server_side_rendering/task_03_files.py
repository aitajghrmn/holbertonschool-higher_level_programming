#!/usr/bin/python3
"""Display product data from JSON or CSV files in Flask."""

import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file():
    """Read products from JSON file."""
    with open("products.json", "r") as file:
        return json.load(file)


def read_csv_file():
    """Read products from CSV file."""
    products = []

    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)

    return products


@app.route("/products")
def products():
    """Display products from JSON or CSV source."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    error = None
    product_list = []

    if source == "json":
        product_list = read_json_file()
    elif source == "csv":
        product_list = read_csv_file()
    else:
        error = "Wrong source"

    if error is None and product_id:
        product_id = int(product_id)
        product_list = [
            product for product in product_list
            if product["id"] == product_id
        ]

        if len(product_list) == 0:
            error = "Product not found"

    return render_template(
        "product_display.html",
        products=product_list,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

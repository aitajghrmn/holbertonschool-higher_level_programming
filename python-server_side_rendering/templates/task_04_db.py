#!/usr/bin/python3
"""Display product data from JSON, CSV, or SQLite database."""

import csv
import json
import sqlite3
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


def read_sql_database():
    """Read products from SQLite database."""
    products = []

    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()

    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        })

    conn.close()
    return products


@app.route("/products")
def products():
    """Display products from selected source."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    error = None
    product_list = []

    try:
        if source == "json":
            product_list = read_json_file()
        elif source == "csv":
            product_list = read_csv_file()
        elif source == "sql":
            product_list = read_sql_database()
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

    except sqlite3.Error as e:
        error = f"Database error: {e}"
    except Exception as e:
        error = f"Error: {e}"

    return render_template(
        "product_display.html",
        products=product_list,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

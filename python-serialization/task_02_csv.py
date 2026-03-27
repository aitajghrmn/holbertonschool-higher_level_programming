#!/usr/bin/python3
'''
Docstring for python-serialization.task_02_csv
'''
import csv, json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as file:
            data = list(csv.DictReader(file))
        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True
    except FileNotFoundError:
        return False

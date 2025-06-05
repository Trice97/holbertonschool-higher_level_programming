#!/usr/bin/python3
"""Module to creat object from a JSON file"""


import json


def load_from_json_file(filename):
    """Function to create an object from a json file"""


    with open(filename, "r") as file:
        return json.load(file)

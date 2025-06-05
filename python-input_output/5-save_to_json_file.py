#!/usr/bin/python3
"""Module for saving objects to JSON files"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)

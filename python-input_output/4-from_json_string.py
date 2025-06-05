#!/usr/bin/python3
"""Module regarding JSON deserialization"""


import json


def from_json_string(my_str):
    """Function that converts JSON string to Python object"""
    return json.loads(my_str)

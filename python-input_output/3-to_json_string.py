#!/usr/bin/python3
"""Module regarding Json """


import json


def to_json_string(my_obj):
    """Function  trat returns the Json representation of an object (string)"""

    return json.dumps(my_obj)

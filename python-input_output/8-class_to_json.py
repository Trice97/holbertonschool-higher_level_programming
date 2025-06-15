#!/usr/bin/python3
"""Module to convert a class into a json dict"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    return obj.__dict__

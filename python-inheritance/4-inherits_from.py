#!/usr/bin/python3
"""Module regarding if a class inherit or no from a specified class"""


def inherits_from(obj, a_class):
    """function in order to check the origin of the object"""

    return isinstance(obj, a_class) and type(obj) is not a_class

#!/usr/bin/python3
"""
Module containing a function that prints a name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints "My name is <first_name> <last_name>"
    Args:
        first_name: first name (must be a string)
        last_name: last name (must be a string), defaults to empty string
    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))

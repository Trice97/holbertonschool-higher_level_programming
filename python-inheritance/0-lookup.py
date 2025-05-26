#!/usr/bin/python3
"""
This module contains a function that returns the list of available
attributes and methods of an object using introspection.
"""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    This function uses the built-in dir() function to get all attributes
    and methods of the given object, including inherited ones.

    Args:
        obj: Any Python object to inspect.

    Returns:
        list: A list of strings containing all attribute and method names
              available on the object.
    """
    return dir(obj)

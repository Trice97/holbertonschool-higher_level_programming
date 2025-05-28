#!/usr/bin/python3
"""That module check if the instance is the object of an speciefied object"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.
    Args:
    Obj: The object to check
    a_class: The class to compare against

    Returns:
    True if obj is exactly an instance of a_class, false ortherwise
    """
    return type(obj) is a_class

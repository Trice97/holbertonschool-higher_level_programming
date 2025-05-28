#!/usr/bin/python3
"""Module for checking object class inheritance."""


def is_kind_of_class(obj, a_class):
    """
    Check if object is instance of or inherits from class

    Args:
        obj: Object to check
        a_class: Class to compare against
        Returns:
        True if obj is instance or inherits from a_class, False otherwise
    """
    return isinstance(obj, a_class)

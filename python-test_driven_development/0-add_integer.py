#!/usr/bin/python3
"""
Module containing function to add two integers
"""


def add_integer(a, b=98):
    """
    Function that adds two integers
    Args:
        a: first number
        b: second number, defaults to 98
    Returns:
        The addition of a and b
    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)

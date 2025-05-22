#!/usr/bin/python3
"""
Module 1-square
This module defines a Square class with a private size attribute.
"""


class Square:
    """
    This class defines a square by a private size attribute.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
        # argument of the instance is set to private

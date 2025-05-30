#!/usr/bin/python3
"""Module that defines a Square class that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """
        Initialize a Square instance.
        Args:
            size (int): The size of the square (must be positive integer)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return string representation of the square.

        Returns:
            str: String in format [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

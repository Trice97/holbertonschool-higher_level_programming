#!/usr/bin/python3
"""Module that defines a Rectangle class that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width (must be positive integer)
            height (int): The height  (must be positive integer)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return string representation of the rectangle.

        Returns:
            str: String in format [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

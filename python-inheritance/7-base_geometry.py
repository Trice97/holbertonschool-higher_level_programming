#!/usr/bin/python3
"""
Module 7-base_geometry.py: Defines the BaseGeometry class.
"""


class BaseGeometry:
    """BaseGeometry class for geometric operations."""

    def area(self):
        """Raises an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.

        Args:
            name (str): The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

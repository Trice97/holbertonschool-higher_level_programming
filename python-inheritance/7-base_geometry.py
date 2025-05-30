#!/usr/bin/python3
"""Module that defines BaseGeometry class with area and integer validator."""


class BaseGeometry:
    """BaseGeometry class with area method and integer validator."""

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: Always with message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is a positive integer.

        Args:
            name (str): The name of the parameter
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

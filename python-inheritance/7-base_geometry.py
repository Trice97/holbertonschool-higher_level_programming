#!/usr/bin/python3
"""
Module 7-base_geometry.py: Defines the BaseGeometry class.

This module provides a foundational class for geometric shapes,
including a method for validating integer values.
"""


class BaseGeometry:
    """
    BaseGeometry class: Serves as a base class for geometric operations.

    It includes a method to raise an exception for area calculation
    and a robust integer validation method.
    """

    def area(self):
        """
        Calculates the area of the geometry.

        This method is not yet implemented in the base class and
        is intended to be overridden by subclasses.
        It raises an Exception to indicate that implementation is pending.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value to ensure it is an integer greater than 0.

        Args:
            name (str): The name of the value, always assumed to be a string.
            value (int): The value to be validated.

        Raises:
            TypeError: If 'value' is not an integer, with the message
                       "<name> must be an integer".
            ValueError: If 'value' is less than or equal to 0, with the message
                        "<name> must be greater than 0".
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

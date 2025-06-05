#!/usr/bin/python3
"""Module that defines a BaseGeometry class."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Calculate area - raises exception as not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.
        
        Args:
            name (str): name of the parameter
            value: value to validate
            
        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

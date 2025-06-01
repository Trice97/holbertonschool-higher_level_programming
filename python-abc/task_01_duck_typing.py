#!/usr/bin/env python3
"""Module for Shape abstract base class, Circle, Rectangle implementations."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Compute and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Compute and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape, defined by its radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape, defined by its width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of any shape (duck typing)."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

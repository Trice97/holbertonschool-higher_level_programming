#!/usr/bin/python3
"""Module that defines a MyList class that inherits from list."""


class MyList(list):
    """MyList class that inherits from list with additional functionality."""

    def print_sorted(self):
        """
        Print the list in ascending sorted order.

        The original list is not modified, only the printed output is sorted.
        All elements are assumed to be integers.
        """
        print(sorted(self))

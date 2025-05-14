#!/usr/bin/python3
# Function that adds 2 tuples

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds 2 tuples element-wise.

    Args:
        tuple_a: First tuple (default empty tuple)
        tuple_b: Second tuple (default empty tuple)

    Returns:
        A new tuple with 2 integers where:
        - First element is the sum of first elements from both tuples
        - Second element is the sum of second elements from both tuples
        - Missing elements in tuples are considered as 0
    """
    # Ensure tuples have at least 2 elements, filling with zeros if needed
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Create new tuple with the sums of first 2 elements
    return (a[0] + b[0], a[1] + b[1])

#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C from a string.

    Args:
        my_string: The input string.

    Returns:
        A new string with all occurrences of 'c' and 'C' removed.
    """
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string

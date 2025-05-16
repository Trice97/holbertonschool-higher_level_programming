#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.
    Args:
        a_dictionary: The input dictionary
        key: The key to update or add (always a string)
        value: The value to associate with the key (any type)
    Returns:
        The updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary

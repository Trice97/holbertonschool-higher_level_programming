#!/usr/bin/python3
# Function that returns a tuple with length of a string and its first character


def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.

    Args:
        sentence: The input string

    Returns:
        A tuple with:
        - The length of the string
        - The first character of the string, or None if string is empty
    """
    length = len(sentence)
    first = sentence[0] if length > 0 else None
    return (length, first)

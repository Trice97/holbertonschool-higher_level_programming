#!/usr/bin/python3
"""
Module containing a function that adds indentation to text
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text: text to print (must be a string)
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Replace characters with the same character followed by 2 newlines
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n\n", end="")
            # Skip spaces after special characters
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

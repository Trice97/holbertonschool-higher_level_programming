#!/usr/bin/python3

def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ['.', '?', ':']
    lines = []
    current_line = ""
    for char in text:
        current_line += char
        if char in delimiters:
            lines.append(current_line.strip())
            current_line = ""
    if current_line:
        lines.append(current_line.strip())

    for line in lines:
        print(line)
        if line[-1] in delimiters:
            print("\n")

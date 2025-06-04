#!/usr/bin/python3
"""Module to write a file using the write statement"""


def write_file(filename="", text=""):
    """Function to write a string and return the character written"""

    with open(filename, mode="w", encoding="utf-8") as my_file:
        nombre_caracteres = my_file.write(text)
        return nombre_caracteres

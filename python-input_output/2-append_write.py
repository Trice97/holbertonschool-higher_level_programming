#!/usr/bin/python3
"""Module to append a string"""


def append_write(filename="", text=""):
    """Function to append a string at the end of a txt file"""
    with open(filename, mode="a", encoding="utf-8") as my_file:
        nbr_characters = my_file.write(text)
        return nbr_characters

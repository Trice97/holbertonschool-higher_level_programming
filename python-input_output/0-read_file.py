#!/usr/bin/python3
"""module to write a function that read a utf-8 text and prints its stdout"""


def read_file(filename=""):
    """ Function allowing the reading of the file"""

    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())

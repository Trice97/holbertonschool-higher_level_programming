#!/usr/bin/python3
"""Module with Student class"""


class Student:
    """Classe qui définit un étudiant"""

    def __init__(self, first_name, last_name, age):
        """Initialise un étudiant"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of the Student"""
        return self.__dict__

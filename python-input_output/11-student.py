#!/usr/bin/python3
"""Module with Student class that supports serialization and deserialization"""


class Student:
    """Class that defines a student with complete serialization support"""
    
    def __init__(self, first_name, last_name, age):
        """Initialize a student with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        
        Args:
            attrs: List of attribute names to retrieve. If None, retrieves all.
        
        Returns:
            Dictionary representation of the student
        """
        if attrs is None:
            return self.__dict__
        
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        
        return self.__dict__
    
    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        
        Args:
            json: Dictionary containing attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)

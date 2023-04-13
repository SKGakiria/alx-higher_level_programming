#!/usr/bin/python3
"""
The 9-student module
A class Student that defines a student
"""


class Student:
    """
    Represents the Student class.
    """
    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary"""
        return self.__dict__

#!/usr/bin/python3
"""
The 11-student module
A class Student that defines a student(based on 10-student.py)
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

    def to_json(self, attrs=None):
        """Retrieves a dictionary"""
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for attr, value in (self.__dict__).items():
                if attr in attrs:
                    my_dict[attr] = value
            return my_dict

    def reload_from_json(self, json):
        """ Replaces all attributes"""
        for attr, value in json.items():
            setattr(self, attr, value)

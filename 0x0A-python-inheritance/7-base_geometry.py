#!/usr/bin/python3
"""
The 7-base_geometry module
a BaseGeometry class (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """
    Represents a base geometry class.
    """
    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raises a TypeError and ValueError exception."""
        if type(value) != int:
            raise TypeError(name + "  must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")

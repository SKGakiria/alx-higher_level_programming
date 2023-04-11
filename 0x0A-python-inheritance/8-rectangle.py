#!/usr/bin/python3
"""
The 8-rectangle module
a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents the creation of a subclass Rectangle of BaseGeometry."""
    def __init__(self, width, height):
        """width and height must be private as well as positive integers."""
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

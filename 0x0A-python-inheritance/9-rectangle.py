#!/usr/bin/python3
"""
The 9-rectangle module
a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)
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

    def area(self):
        """Returns the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the printable string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

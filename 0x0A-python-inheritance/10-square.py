#!/usr/bin/python3
"""
The 10-square module
a class Square that inherits from Rectangle (9-rectangle.py).
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents the creation of a subclass Square of Rectangle."""
    def __init__(self, size):
        """size must be private as well as positive integers."""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

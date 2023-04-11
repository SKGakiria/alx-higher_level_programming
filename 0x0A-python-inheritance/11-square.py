#!/usr/bin/python3
"""
The 11-square module
a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents the creation of a subclass Square of Rectangle."""
    def __init__(self, size):
        """size must be private as well as positive integers."""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns the printable string representation of the Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)

#!/usr/bin/python3
"""Defining a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle.
        Args:
           height (int): The height of the rectangle
           width (int): The width of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Used for retrieving the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Raises:
            TypeError exception: If width value isn't integer.
            ValueError exception: If width is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Used for retrieving the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Raises:
            TypeError exception: If height value isn't integer.
            ValueError exception: If height is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

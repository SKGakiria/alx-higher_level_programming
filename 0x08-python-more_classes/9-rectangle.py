#!/usr/bin/python3
"""Defining a Rectangle class."""


class Rectangle:
    """Represents a rectangle.
    Attributes:
        number_of_instances (int): The number of instances.
        print_symbol (any): Symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle.
        Args:
           height (int): The height of the rectangle
           width (int): The width of the rectangle
        """
        type(self).number_of_instances += 1
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

    def area(self):
        """Returns the rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.
        Args:
            rect_1: The first rectangle
            rect_2: The second rectangle
        Raises:
            TypeError exception: If neither rect_1 nor rect_2 is a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle with size equal to width and height.
        Args:
           size (int): width and height of new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """Returns printed rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returns a string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """For every delection of a Rectangle, print a message."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

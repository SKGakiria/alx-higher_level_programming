#!/usr/bin/python3
"""
The almost a circle module
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents the Rectangle class a subclass of Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Used for retrieving the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Raises:
            TypeError exception: If width value isn't integer.
            ValueError expception: If width is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
            ValueError expception: If height is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Used for retrieving x."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Raises:
            TypeError exception: If x value isn't integer.
            ValueError expception: If x is < 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Used for retrieving y."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Raises:
            TypeError exception: If y value isn't integer.
            ValueError expception: If y is < 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the rectangle area."""
        return self.width * self.height

    def display(self):
        """Prints the rectangle using the '#' character."""
        pattern = ""
        if self.width == 0 or self.height == 0:
            print(pattern)
        else:
            for y in range(self.y):
                pattern += '\n'
            for h in range(self.height):
                for x in range(self.x):
                    pattern += ' '
                for w in range(self.width):
                    pattern += '#'
                if h != (self.height - 1):
                    pattern += '\n'
            print(pattern)

    def __str__(self):
        """String representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Updating the rectangle."""
        my_list = ["id", "width", "height", "x", "y"]
        if args and len(args) != 0:
            i = 0
            for i, arg in enumerate(args):
                setattr(self, my_list[i], arg)
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.iems():
                setattr(self, k, v)

    def to_dictionary(self):
        """Dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

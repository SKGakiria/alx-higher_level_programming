#!/usr/bin/python3
"""
The almost a circle module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents the Square class a subclass of Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Used for retrieving the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating the square."""
        my_list = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            i = 0
            for i, arg in enumerate(args):
                setattr(self, my_list[i], arg)
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

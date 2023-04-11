#!/usr/bin/python3
"""Defines a function that adds a new attribute to an object."""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it’s possible.
    Args:
      obj (any): The object where the attribute is to be added.
      name (str): The name of the attribute to be added to obj.
      value (any): The value of the name.
    Raises:
      TypeError exception: If the attribute cannot be added.
    """
    for element in dir(obj):
        if element == '__dict__':
            setattr(obj, name, value)
            return
    raise TypeError("can't add new attribute")

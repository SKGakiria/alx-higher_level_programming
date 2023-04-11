#!/usr/bin/python3
"""
The 4-inherits_from
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an instance of a
    class that inherited (directly or indirectly) from the specified
    class ; otherwise False.
    """
    if isinstance(obj, a_class):
        if issubclass(a_class, obj.__class__) is not True:
            return True
    return False

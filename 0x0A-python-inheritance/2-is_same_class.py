#!/usr/bin/python3
"""
The 2-is_same_class module
"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object is exactly an instance
    of the specified class ; otherwise False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False

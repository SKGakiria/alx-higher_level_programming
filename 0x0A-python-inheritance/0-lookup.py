#!/usr/bin/python3
"""
The 0-lookup module
"""


def lookup(obj):
    """
    Function that returns the list of available attributes
    and methods of an object.
    """
    return dir(obj)

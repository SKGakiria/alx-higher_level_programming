#!/usr/bin/python3
"""Defines a name printing function"""


def say_my_name(first_name, last_name=""):
    """Prints names.
    Args:
        first_name (str): first name to be printed.
        last_name (str): last name to be printed.
    Raises:
        TypeError exception: If first_name and last_name aren't strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last__name must be a string")
    print("My name is {} {}".format(first_name, last_name))

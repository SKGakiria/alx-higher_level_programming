#!/usr/bin/python3
"""
The 100-my_int module
a class MyInt that inherits from int
"""


class MyInt(int):
    """Represents the creation of a subclass MyInt of int."""
    def __eq__(self, value):
        """Myint is equal to."""
        return False

    def __ne__(self, value):
        """Myint is different to."""
        return True

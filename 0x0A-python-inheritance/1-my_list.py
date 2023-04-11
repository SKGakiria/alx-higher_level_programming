#!/usr/bin/python3
"""
The 1-my_list module
a class MyList that inherits from list.
"""


class MyList(list):
    """
    Public instance method: def print_sorted(self):
    that prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        """prints the sorted list."""
        return print(sorted(self))

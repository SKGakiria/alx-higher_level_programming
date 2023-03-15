#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary."""
    try:
        a_dictionary.pop(key)
    except KeyError:
        pass
    return a_dictionary

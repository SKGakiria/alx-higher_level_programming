#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""
    try:
        delete = []
        for key in a_dictionary:
            if a_dictionary[key] == value:
                delete.append(key)
        for key in delete:
            a_dictionary.pop(key)
    except (KeyError, RuntimeError):
        pass
    return a_dictionary

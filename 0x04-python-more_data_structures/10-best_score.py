#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if a_dictionary:
        sorted_dict = sorted(a_dictionary.items(), key=lambda item: item[1])
        return (sorted_dict[-1])[0]
    else:
        return None

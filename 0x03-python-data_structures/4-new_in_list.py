#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position without modifying the original list."""
    copy = []
    for num in my_list:
        copy.append(num)
    if idx < 0:
        return copy
    elif idx >= len(my_list):
        return copy
    else:
        copy[idx] = element
        return copy

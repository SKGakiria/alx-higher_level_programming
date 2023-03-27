#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers."""
    count = 0
    for val in range(x):
        try:
            print("{:d}".format(my_list[val]), end="")
        except (ValueError, TypeError):
            continue
        else:
            count += 1
    print("")
    return count

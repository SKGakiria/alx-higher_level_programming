#!/usr/bin/python3
"""
The 7-add_item module
"""

import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_items():
    """
    Function that adds all arguments to a Python list,
    and then saves them to a file.
    """
    try:
        my_list = load_from_json_file('add_item.json')
    except:
        my_list = []

    for elem in range(1, len(sys.argv)):
        my_list.append(sys.argv[elem])

    save_to_json_file(my_list, 'add_item.json')


if __name__ == '__main__':
    add_items()

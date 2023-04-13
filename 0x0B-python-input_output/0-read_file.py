#!/usr/bin/python3
"""
The 0-read_file module
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout.
    """
    with open(filename, encoding='UTF-8') as f:
        f_contents = f.read()
        print(f_contents, end='')

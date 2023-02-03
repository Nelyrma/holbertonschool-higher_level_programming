#!/usr/bin/python3
"""
contains a function that prints a square
"""


def print_square(size):
    """
    Prints a square with the character #
    """
    if type(size) is not int:
        raise TypeError("Size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print(size * '#')

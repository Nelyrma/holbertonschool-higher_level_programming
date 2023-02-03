#!/usr/bin/python3
"""
contains a function that adds two integers
"""


def add_integer(a, b=98):
    """
    returns an integer: a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

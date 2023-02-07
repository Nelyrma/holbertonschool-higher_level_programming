#!/usr/bin/python3
"""
contains the is_same_class method
"""


def is_same_class(obj, a_class):
    """
    checks if the object is an instance of a specified class
    """
    return type(obj) is a_class

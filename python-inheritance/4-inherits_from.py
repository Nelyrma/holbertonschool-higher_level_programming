#!/usr/bin/python3
"""
contains an inherits_from method
"""


def inherits_from(obj, a_class):
    """
    checks if an object is a subclass
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))

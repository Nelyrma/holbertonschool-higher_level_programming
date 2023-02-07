#!/usr/bin/python3
"""
contains the lookup(obj) method
"""


def lookup(obj):
    """
    returns a list of available attributes an methods of an object
    """
    return dir(obj)

#!/usr/bin/python3
"""
class that define a square with a private attribute
"""

class Square:
    """
    size : private instance attribute
    """

    def __init__(self, size=0):
        """
        initialisation of a square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

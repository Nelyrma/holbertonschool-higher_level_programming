#!/usr/bin/python3
"""
class that define a square
"""


class Square:
    """
    size : size of a square
    area: public instance method
    """
    def __init__(self, size=0):
        """
        initialize a square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        define the area of a square
        """

        return (self.__size ** 2)

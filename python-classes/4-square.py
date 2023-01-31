#!/usr/bin/python3
"""
class that define a square
"""


class Square:
    """
    size: private instance attribute
    area: public instance method
    """

    def __init__(self, size=0):
        """
        initialize a square
        """
        self.__size = size

    @property
    def size(self):
        """
        retrieve the size of a square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        set the value of size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        define the area of a square
        """
        return (self.__size ** 2)

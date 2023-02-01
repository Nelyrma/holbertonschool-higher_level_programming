#!/usr/bin/python3
"""
contains a class Rectangle
"""


class Rectangle:
    """
    defines a rectangle by:
    Private instance attribute: width
    Private instance attribute: height
    """
    def __init__(self, width=0, height=0):
        """
        initializes a rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        retrieves the width instance attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width value of a rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        retrieves the height instance attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height value of a rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

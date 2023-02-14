#!/usr/bin/python3
"""class Rectangle that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """
    class Rectangle

    Private instance attributes:
        __width (int)
        __height (int)
        __x (int): x-coordinate of the rectangle
        __y (int): y-coordinate of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """retrieves the width instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value of a rectangle"""
        self.__width = value

    @property
    def height(self):
        """retrieves the  height instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height value of a rectangle"""
        self.__height = value

    @property
    def x(self):
        """retrieves the x instance attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x value"""
        self.__x = value

    @property
    def y(self):
        """retrieves the y intance attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y value"""
        self.__y = value

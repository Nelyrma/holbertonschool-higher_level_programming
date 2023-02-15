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
        """
        class constructor

        Args:
            width
            height
            x
            y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieves the width instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value of a rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the  height instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height value of a rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieves the x instance attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieves the y intance attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the rectangle instance with the character #"""
        rect = "\n".join(["#" * self.__width for rows in range(self.__height)])
        print(rect)

    def __str__(self):
        """overriding the __str__ method"""
        return '[Rectangle] ({}) {}/{} - {}/{}' \
            .format(self.id, self.x, self.y, self.width, self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Internal method that updates instance attributes via */**args """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args):
        """public method that assigns an argument to each attribute"""
        if args:
            self.__update(*args)

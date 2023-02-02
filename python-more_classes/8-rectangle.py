#!/usr/bin/python3
"""
contains a class Rectangle
"""


class Rectangle:
    """
    Defines a class rectangle with private attribute width and height
    Args:
        width (int): width
        height (int): height
    Attributes:
        number_of_instances (int): number of instances created and not deleted
        print_symbol: used as symbol for string representation
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
        bigger_or_equal(rect_1, rect_2): static method
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initializes a rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """
        returns the area of a rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        returns the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """
        prints the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = "\n".join([str(self.print_symbol) * self.__width
                         for rows in range(self.__height)])
        return rect

    def __repr__(self):
        """
        returns a string representation"
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """
        delete an instance
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

#!/usr/bin/python3
"""
module for subclass Square that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a subclass Square"""
    def __init__(self, size):
        """constructor for square"""
        self.integer_validator('size', size)

        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

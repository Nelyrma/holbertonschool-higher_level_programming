#!/usr/bin/python3
"""
contains a subclass Rectangle that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    defines a subclass Rectangle
    """
    def __init__(self, width, height):
        """
        constructor for rectangle
        """
        self.__width = width
        self.__height = height

        self.integer_validator('width', width)
        self.integer_validator('height', height)

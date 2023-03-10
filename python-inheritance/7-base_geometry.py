#!/usr/bin/python3
"""
contains a BaseGeometry class
"""


class BaseGeometry:
    """
    Defines a class BaseGeometry
    Functions:
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        """
        raises an exception with a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates the value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

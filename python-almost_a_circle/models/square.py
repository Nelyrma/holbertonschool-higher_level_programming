#!/usr/bin/python3
"""contains the class Square that inherits from Rectangle"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding the __str__ method"""
        phrase = "[Square] ({}) {}/{} - {}"
        return phrase.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """retrieves the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size value of a square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
            self.height = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.width = value
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

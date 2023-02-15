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


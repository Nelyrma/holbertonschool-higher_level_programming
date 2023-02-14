#!/usr/bin/python3
"""Class Base which is the base of all other classes in this project"""


class Base:
    """create the class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
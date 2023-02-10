#!/usr/bin/python3
"""contains a class Student"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            m = {}
            for i in attrs:
                if i in self.__dict__:
                    m[i] = self.__dict__[i]
            return m
        return self.__dict__

    def reload_from_json(self, json):
        for i in json:
            self.__dict__[i] = json[i]

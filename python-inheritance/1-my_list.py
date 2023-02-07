#!/usr/bin/python3
"""
contains the class MyList
"""


class MyList(list):
    """
    MyList herits from list
    """
    def print_sorted(self):
        """
        prints a sorted list
        """
        print(sorted(self))

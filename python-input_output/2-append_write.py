#!/usr/bin/python3
"""contains a function that appends a string to a file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, "a") as fic:
        fic.write(text)

    return len(text)

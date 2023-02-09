#!/usr/bin/python3
"""contains a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """function that write a string"""
    with open(filename, "w") as fic:
        fic.write(text)

    return len(text)

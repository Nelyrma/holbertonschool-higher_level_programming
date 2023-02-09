#!/usr/bin/python3
"""contains a function that reads a file"""


def read_file(filename=""):
    """Reads a file and prints it to stdout"""

    with open(filename, "r") as fic:
        print(fic.read())

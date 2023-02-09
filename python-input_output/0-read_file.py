#!/usr/bin/python3
"""contains a function that reads a file"""


def read_file(filename=""):
    """Reads a file and prints it to stdout"""

    fic = open(filename, "r")

    content = fic.read()
    print content

    fic.close()

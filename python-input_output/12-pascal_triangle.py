#!/usr/bin/python3
"""
Contains a function that returns a list of lists
of integers  representing the Pascal’s triangle of
a given number
"""


def pascal_triangle(n):
    """Returns a pascal triangle matrix"""
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(len(triangle[i - 1]) - 1):
                row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
            row.append(1)
        triangle.append(row)
    return triangle

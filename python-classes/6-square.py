#!/usr/bin/python3
"""
class that defines a square
"""


class Square:
    """
    Square defines two private instances attributes size and position
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position


    @property
    def size(self):
        """
        retrieve the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the size of a square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value


    @property
    def position(self):
        """
        retrieve the position of a square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        set the position of a square
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value


    def area(self):
        """
        Return the area of a square
        """
        return self.__size ** 2


    def my_print(self):
        """
        Print a square with the character '#'
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))


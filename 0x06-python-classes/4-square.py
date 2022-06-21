#!/usr/bin/python3


# 4-square.py


""" class of square """


class Square:

    """ inside square """
    def __init__(self, size=0):
        """
        Args:
            size (int): integer
        """
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):

        """ area of square """
        return pow(self.__size, 2)

    @size.setter
    def size(self, value):
        if value != int(value):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def size(self):
        """ getter """
        return self.__size

#!/usr/bin/python3


# 6-square.py


""" class of square """


class Square:

    """ inside square """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size (int): integer
            position (int, int): tuple
        """
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Get and set """
        return self.__size

    @size.setter
    def size(self, value):
        if value != int(value):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ get and set """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Args:
            value (tuple): tuple
        """
        if type(value) is not tuple or len(value) != 2 or not all(isinstance(num, int) for num in value) or all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ area of square """
        return pow(self.__size, 2)

    def my_print(self):
        """ print to stdout """
        for x in range(0, self._position[1]):
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")

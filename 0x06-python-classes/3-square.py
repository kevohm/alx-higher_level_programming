#!/usr/bin/python3
# 3-square.py

"""square class"""

class Square:
    """ inside class"""

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

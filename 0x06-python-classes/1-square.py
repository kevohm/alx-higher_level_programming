#!/usr/bin/python3
# 2-square.py

"""Square."""


class Square:
    """Rep square."""

    def __init__(self, size=0):
        """
        Args:
            size (int): size
        """
        if size != int(size):
<<<<<<< HEAD
            raise TypeError("Not a int")
        if size < 0:
            raise ValueError("Value is invalid")
        self.__size = size
=======
            raise TypeError("size must be of integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
>>>>>>> ddcedebc85d64c4c83d0f6bb549a0b5506ad7ff8

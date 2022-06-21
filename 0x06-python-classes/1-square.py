#!/usr/bin/python3
# 2-square.py

"""class of square"""


class Square:
    """class of square"""

    def __init__(self, size=0):
        """
        Args:
            size (int): size
        """
        if size != int(size):
            raise TypeError("Not a int")
        if size < 0:
            raise ValueError("Value is invalid")
        self.size = size

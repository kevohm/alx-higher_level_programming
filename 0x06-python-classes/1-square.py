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
            raise TypeError("size must be of integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

#!/usr/bin/python3
# 4-print_square.py

'''4-print_square module

prints a square with the character #

'''


def print_square(size):
    '''function print_square
    prints a square with the character #
    '''
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    i = size
    while i > 0:
        j = size
        while j > 0:
            print("#", end="")
            j -= 1
        print()
        i -= 1

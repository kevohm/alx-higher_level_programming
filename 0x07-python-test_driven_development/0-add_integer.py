#!/usr/bin/python3
# 0-add_integer.py

"""add_integer module

This module add two integers and rounds float

"""


def add_integer(a, b=98):
    ''' add_integer function
    Return: result of  a plus b
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(round(a)) + int(round(b))

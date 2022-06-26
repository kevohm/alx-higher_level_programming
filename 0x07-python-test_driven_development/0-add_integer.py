#!/usr/bin/python3
# 0-add_integer.py

""" add_integer module """


def add_integer(a, b=98):
    '''
    Args:
        a (int): integer
        b (int): integer
    Returns:
        int: a plus b
    '''
    if not isinstance(a,(int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b,(int, float)):
        raise TypeError("b must be an integer")
    return int(round(a)) + int(round(b))

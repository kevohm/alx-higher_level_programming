#!/usr/bin/python3
# multiple_returns

def multiple_returns(sentence):
    """multiple_returns"""
    length = len(sentence)
    last = None
    if (length > 0):
        last = sentence[-1]
    return (length, last)

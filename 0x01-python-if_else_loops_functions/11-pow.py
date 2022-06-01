#!/usr/bin/python3

def pow(a, b):
    if(b < 0):
        b = abs(b)
        a = 1 / a
    if(b == 0):
        return(1)
    b -= 1
    return round((a *  pow(a, b)), 2)

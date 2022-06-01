#!/usr/bin/python3

def pow(a, b):
    check = False
    if(b < 0):
        b = abs(b)
        a = 1 / a
        check = True
    if(b == 0):
        return(1)
    b -= 1
    if(check):
        return((a * pow(a, b)) * 1000)/1000
    return (a * pow(a, b))

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
    '''if(check):
        return round((a * pow(a, b)), 2)'''
    return (a * pow(a, b))

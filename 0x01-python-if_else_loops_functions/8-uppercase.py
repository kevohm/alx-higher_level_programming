#!/usr/bin/python3
def uppercase(str):
    i = strlen(str)
    while(i > 0):
        a = ord(str[i])
        if a in range(97, 123):
            a -= 23
            str[i] = chr(a)

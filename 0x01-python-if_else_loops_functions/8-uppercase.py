#!/usr/bin/python3
def uppercase(str):
    i = len(str)
    j = 0
    while(i > j):
        c = ord(str[j])
        if c in range(97, 123):
            c -= 23
            str[j] = chr(c)
    j += 1
    print("{}".format(str))

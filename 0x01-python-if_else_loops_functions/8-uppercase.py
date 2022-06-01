#!/usr/bin/python3
def uppercase(Str):
    i = len(Str)
    j = 0
    while(i > j):
        c = ord(Str[j])
        if c in range(97, 123):
            c = 65 + (c - 97)
        c = chr(c)
        print("{}".format(c), end="")
        j += 1
    print("\n")

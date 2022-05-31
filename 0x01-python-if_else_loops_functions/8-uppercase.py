#!/usr/bin/python3
def uppercase(Str):
    i = len(Str)
    j = 0
    output = ""
    while(i > j):
        c = ord(Str[j])
        if c in range(97, 123):
            c -= 23
        output += str(chr(c))
    j += 1
    print("done")
    print("{}".format(output))

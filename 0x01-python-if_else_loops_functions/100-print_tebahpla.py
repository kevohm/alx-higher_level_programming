#!/usr/bin/python3
for c in range(122,98,-1):
    if(c % 2 != 0):
        c = 65 + (c - 97)
    print("{}".format(c), end=(""))

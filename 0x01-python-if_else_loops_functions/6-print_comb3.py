#!/usr/bin/python3
for i in range(1, 90):
    check = True
    q = i % 10
    m = i / 10
    m += (10 * q)
    for j in range(1, 10):
        j += (10 * j)
        if (i == j):
            check = False
    if (m >= i and check):
        print("{}".format(i), end=", ")

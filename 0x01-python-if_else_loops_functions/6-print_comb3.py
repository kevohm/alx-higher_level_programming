#!/usr/bin/python3
for i in range(1, 90):
    q = i % 10
    m = i / 10
    m += (10 * q)
    for j in range(1, 10):
        j += (10 * j)
        print(j)
        if (i == j):
            pass
    if (m >= i):
        print("{}".format(i), end=", ")

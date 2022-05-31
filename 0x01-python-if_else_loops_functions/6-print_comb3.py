#!/usr/bin/python3
for i in range(1, 89):
    check = True
    q = i % 10
    m = i / 10
    m += (10 * q)
    for j in range(1, 10):
        j += (10 * j)
        if (i == j):
            check = False
    if (m >= i and check):
        if (i < 10):
            i = "0" + str(i)
        print("{}".format(i), end=", ")
print("89")

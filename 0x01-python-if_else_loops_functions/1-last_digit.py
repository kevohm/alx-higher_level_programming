#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
q = abs(number) % 10
if (number < 0):
    q = -q
print("Last digit of {} is {}".format(number, q), end=" ")
if (q > 5):
    print("and is greater than 5")
elif (q == 0):
    print("and is 0")
else:
    print("and is less than 6 and not 0")

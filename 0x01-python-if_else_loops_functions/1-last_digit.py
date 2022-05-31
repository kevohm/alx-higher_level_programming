#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
q = number % 10

if (q > 5):
    print("Last digit of {} is {} and is greater than 5".format(number, q))
elif (q == 0):
    print("Last digit of {} is {} and is 0".format(number, q))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, q))

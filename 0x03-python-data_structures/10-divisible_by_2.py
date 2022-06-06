#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    cpy = my_list
    for i in range(len(my_list)):
        if((my_list[i] % 2) == 0):
            cpy[i] = True
        else:
            cpy[i] = False
    return (cpy)



#!/usr/bin/python3
# max_integer
def max_integer(my_list=[]):
    max_val = 0
    for i in range(len(my_list)):
        if(my_list[i] > max_val):
            max_val = my_list[i]
    return max_val

#!/usr/bin/python3
# max_integer
def max_integer(my_list=[]):
    max_val = 0
    if len(my_list) == 0:
        return None
    for i in range(len(my_list)):
        if(my_list[i] > max_val):
            max_val = my_list[i]
    return max_val

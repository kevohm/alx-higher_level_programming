#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    if length > 0:
        for i in range(length/2):
            temp = my_list[i]
            my_list[i] = my_list[length - i]
            my_list[length - i] = temp

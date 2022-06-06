#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """Print all int of a lst in reverse order."""
    my_list = my_list[::-1]
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))

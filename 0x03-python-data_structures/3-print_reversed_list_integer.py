#!/usr/bin/python3
# print_reversed_list_integer


def print_reversed_list_integer(my_list=[]):
    """Print all int of a lst in reverse order."""
    if len(my_list) != 0:
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))

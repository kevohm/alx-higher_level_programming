#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """ print reversed """
    try:
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))
    except TypeError:
        return


if __name__ == "__main__":
    pass

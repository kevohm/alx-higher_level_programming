#!/usr/bin/python3
# print_matrix_integer

def print_matrix_integer(matrix=[[]]):
    """ print matrix """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if i != (len(matrix[i]) - 1):
                print("", end=" ")

        print("")

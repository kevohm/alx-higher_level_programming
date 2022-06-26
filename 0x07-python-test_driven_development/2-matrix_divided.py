#!/usr/bin/python3
# 2-matrix_divided.py
'''matrix_divided module

outputs all values of matrix divided by div

'''


def matrix_divided(matrix, div):
    '''matrix_divided function
    Return: a new matrix
    '''
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(message)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div <= 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(message)
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, (int, float)):
                raise(message)
    return [[round(i/3, 2) for i in j]for j in matrix]

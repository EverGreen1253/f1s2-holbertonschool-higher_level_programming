#!/usr/bin/python3
"""
This module contains one function for dividing all elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    Sums up the arguments passed in.

    Args:
        matrix (array) : 2d array
        3 (int) : the divisor

    Returns:
        array: all values inside are divided by the divisor
    """

    new_matrix = matrix.copy()
    rowlength = len(new_matrix[0])
    mat_err = "matrix must be a matrix (list of lists) of integers/floats"

    for i in range(len(new_matrix)):
        if len(new_matrix[i]) != rowlength:
            raise TypeError("Each row of the matrix must have the same size")

        for j in range(len(new_matrix[i])):
            if (isinstance(new_matrix[i][j], int) is not True and 
                    isinstance(new_matrix[i][j], float) is not True):
                raise TypeError(mat_err)

    if isinstance(div, int) is not True and isinstance(div, float) is not True:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(new_matrix)):
        new_matrix[i] = [round(i/div, 2) for i in new_matrix[i]]

    return new_matrix

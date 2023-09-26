#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Prints out a matrix (2d array)."""

    if len(matrix) == 0:
        return None

    new_matrix = [None] * len(matrix)

    i = 0
    while i < len(matrix):
        j = 0
        temp = [None] * len(matrix[i])
        while j < len(matrix[i]):
            temp[j] = matrix[i][j] * matrix[i][j]
            j = j + 1

        new_matrix[i] = temp
        i = i + 1

    return new_matrix

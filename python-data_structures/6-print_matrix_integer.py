#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints out a matrix (2d array)."""

    if len(matrix) == 0:
        return None

    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if j != 0:
                print(" ", end="")

            print("{:d}".format(matrix[i][j]), end="")
            j = j + 1
        print("")
        i = i + 1

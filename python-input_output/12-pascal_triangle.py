#!/usr/bin/python3
"""Module docstring goes here"""


def pascal_triangle(n):
    """Make a Pascal's Triangle

    Args:
        n (int): number of layers

    Returns:
        Representation of the triangle using lists

    """

    triangle = [None] * n

    for i in range(n):
        triangle[i] = [None] * (i + 1)

        value = 1
        for j in range(i + 1):
            if i > 0:
                #check prev row
                if len(triangle[i - 1]) >= (j + 1) and j != 0:
                    value = triangle[i - 1][j] + triangle[i - 1][j - 1]
                else:
                    value = 1

            triangle[i][j] = value

    return triangle

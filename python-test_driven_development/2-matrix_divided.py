#!/usr/bin/python3
"""Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div."""
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]

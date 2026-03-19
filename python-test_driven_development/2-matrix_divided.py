#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix: list of lists of integers/floats
        div: number (int or float)

    Returns:
        new matrix with elements divided by div, rounded to 2 decimals
    """

    # Check matrix structure
    if (not isinstance(matrix, list) or
        len(matrix) == 0 or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check all rows same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check div type
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        new_matrix.append(new_row)

    return new_matrix

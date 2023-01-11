#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix."""
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if isinstance(matrix[i][j], int):
                matrix[i][j] = matrix[i][j] ** 2
    return matrix

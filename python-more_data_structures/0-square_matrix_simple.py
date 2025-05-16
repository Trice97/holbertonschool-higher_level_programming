#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    Returns a new matrix with same size as matrix where each value
    is the square of its corresponding value in the input matrix.
    """
    new_matrix = []

    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value ** 2)
        new_matrix.append(new_row)

    return new_matrix

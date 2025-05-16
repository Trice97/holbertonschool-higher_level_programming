#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    Returns a new matrix with same size as matrix where each value
    is the square of its corresponding value in the input matrix.
    """
    # Create a new matrix with the same structure as the input
new_matrix = []
# For each row in the matrix
    for row in matrix:
        # Create a new row with squared values
        new_row = []
        for value in row:
            new_row.append(value ** 2)
        # Add the new row to the new matrix
        new_matrix.append(new_row)
    return new_matrix

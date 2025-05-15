#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.

    Args:
        matrix: A 2 dimensional array (list of lists) of integers.

    Returns:
        A new matrix: Same size as matrix
        Each value should be the square of the value of the input
        Initial matrix should not be modified
    """
    if not matrix:
        return []

    new_matrix = [[x**2 for x in row] for row in matrix]
    return new_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)

#!/usr/bin/python3
"""
Module containing a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    Args:
        matrix: a list of lists of integers or floats
        div: number to divide the matrix by
    Returns:
        A new matrix with all elements divided by div
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If each row of the matrix doesn't have the same size
        TypeError: If div is not a number (integer or float)
        ZeroDivisionError: If div is equal to 0
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = None
    for row in matrix:
        # Check if row is a list
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        # Check if row size is the same as previous rows
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        
        # Check if elements are integers or floats
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is not 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide all elements of the matrix by div
    return [[round(elem / div, 2) for elem in row] for row in matrix]

#!/usr/bin/python3
# Function that prints a matrix of integers
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, col in enumerate(row):
            # Print without space if it's the last element in the row
            if i == len(row) - 1:
                print("{:d}".format(col), end="")
            else:
                print("{:d}".format(col), end=" ")
        print()

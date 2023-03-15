#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix."""
    new_matrix = []
    for num in matrix:
        new_num = list(map(lambda x: x ** 2, num))
        new_matrix.append(new_num)

    return new_matrix

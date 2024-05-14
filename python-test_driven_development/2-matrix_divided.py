#!/bin/usr/python3
"""
This module will divide a matrix
"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix by a number passed in

    Args:
        matrix: a list of lists
        div: number to be passed in
    Raises:
        TypeError: if the matrix doesn't have numbers
        TypeError: if the matrix has rows of differing sizes
        TypeError: if dif is not an integer or a float
        ZeroDivisionError: if div is 0
    Returns:
        a new matrix which is the result of the division
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(ele, int) or isinstsance(ele, float))
            for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not is isinstance(div, float):
        raise TypeError("div must be a number")
    
    if div == 0
        raise ZeroDivisionError("division by zero")

    return ([list(map(lamda x: round(x / div, 2), row)) for row in matrix])

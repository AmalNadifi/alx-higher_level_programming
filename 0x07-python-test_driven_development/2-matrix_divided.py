#!/usr/bin/python3
""" Definition of a module to  divide all elements of a matrix """


def matrix_divided(matrix, div):
    """ This function to divide the elements of a matrix by a given number

    Args:
        matric (list): The list of lists of integers or floats
        div (int or float): The dividing number

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
        TypeError: If matrix rows don't have the same size
        TypeError: If div is not int or float
        ZeroDivisionError: If div is zero

    Returns:
        list: A new resultant matrix
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list)
            for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
               " of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(a / div, 2) for a in row] for row in matrix]

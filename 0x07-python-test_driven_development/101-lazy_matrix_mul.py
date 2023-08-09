#!/usr/bin/python3
""" Definition of function for matrix multiplication while using NumPy"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ The function returns the resultant multiplication of the two matrices

    Args:
        m_a: The first matrix
        m_b: the second matrix

    Returns:
        list: the resultant matrix
    """

    return np.dot(m_a, m_b)

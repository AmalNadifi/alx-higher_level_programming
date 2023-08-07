#!/usr/bin/python3
""" Definition of a module to print a square with '#' character """


def print_square(size):
    """ The function prints a square using the character '#' based on
    the given size

    Args:
        size (int): Size of the square

    Raises:
        TypeError: if the given size is not integer
        ValueError: if the given size is < 0

    Returns:
        None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for itr in range(size):
        print('#' * size)

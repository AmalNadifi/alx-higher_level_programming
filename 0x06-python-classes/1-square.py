#!/usr/bin/python3
""" Definition of a class Square"""


class Square:
    """ This class represents a Square

    Attributes:
    __size (int): Size of the square as a private instance attribute
    """

    def __init__(self, size):
        """
        Initialization of the Square instance with the given size
        Args:
        size (int): The size of the square
        """
        self.__size = size

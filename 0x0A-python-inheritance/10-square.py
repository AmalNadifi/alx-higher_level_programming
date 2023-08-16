#!/usr/bin/python3
""" Definition of a subclass of Rectangle named 'Square' """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This function represents a square"""
    def __init__(self, size):
        """ Initilization of a new square

        Args:
            size (int): the new square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

#!/usr/bin/python3
""" Definition of a class Rectangle inherited from Rectangle """
Rectangle = __import__('9-rectangle').rectangle


class Square(Rectangle):
    """ This class is representing a Square using Rectangle """

    def __init__(self, size):
        """ This function initilizes a new square

        Args:
            size (int): The new square size
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ This function returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """ This function returns the print() and str() representation
        of the square
        """
        return f"[Square] {self.__size}/{self.__size}"

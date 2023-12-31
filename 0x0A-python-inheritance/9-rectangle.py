#!/usr/bin/python3
""" Definition of a class Rectangle inherited from Basegeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This class is representing a rectangle using BaseGeometry """

    def __init__(self, width, height):
        """ This function initilizes a new rectangle

        Args:
            width (int): The new rectangle width
            height (int): The new rectangle height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ This function returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ This function returns the print(( and str() representation
        of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

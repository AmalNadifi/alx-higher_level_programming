#!/usr/bin/python3
""" Definition of a class Rectangle"""


class Rectangle:
    """ This class represents a rectangle

    Attributes:
        width (int): The rectangle's width
        height (int): The rectangle's height
    """

    def __init__(self, width=0, height=0):
        """
        Initialization of the Rectangle instance.

        Args:
            width (int): The rectangle's width (0 as default)
            height (int): The rectangle's height (0 as default)

        Raises:
            TypeError: If width or height is not int
            ValueError: If width or height < 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get the rectangle's width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for the optional width attribute """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get the rectangle's height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for the optional height attribute """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

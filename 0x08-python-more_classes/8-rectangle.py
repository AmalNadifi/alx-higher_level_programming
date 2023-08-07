#!/usr/bin/python3
""" Definition of a class Rectangle"""


class Rectangle:
    """ This class represents a rectangle

    Attributes:
        width (int): The rectangle's width
        height (int): The rectangle's height
        number_of_instances (int): Public attribute to keep track of instances
    """
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1  # Increment instance counter

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
            raise ValueError("height  must be >= 0")
        self.__height = value

    def area(self):
        """ Calculation of the rectangle area

        Returns:
            int: The rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculation of the rectangle perimeter

        Returns:
            int: The rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ Printing the rectangle using the '#' character

        if width or height is zero, it does print an empty string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join(
                    str(self.print_symbol) * self.__width
                    for x in range(self.__height))

    def __repr__(self):
        """ Returning the string representation of the rectangle able to
        recreate a new instance of rectangle
        Returns:
            str: The rectangle string representation
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Printing a message when a rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Comparing the area of two rectangles

        Args:
            rect_1 (Rectangle): The 1st rectangle to compare
            rect_2 (Rectangle): The 2nd rectangle to compare

        Raises:
            TypeError: If rect_1 or rect_2 is not a rectangle instance

        Returns:
            Rectangle: The biggest rectangle
            or rect_1 if both have the same area value
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect1.area() >= rect_2.area():
            return rect_1
        return rect_2

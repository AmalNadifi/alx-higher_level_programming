#!/usr/bin/python3
""" Definition of a class Rectangle inherited from Base """
from models.base import Base


class Rectangle(Base):
    """ This class is representing a rectangle using "Base" """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ This function initilizes a new rectangle

        Args:
            width (int): The new rectangle width
            height (int): The new rectangle height
            x: the x position
            y : the y position
            id: The instances
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @staticmethod
    def validate_attribute(attribute, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    @property
    def width(self):
        """ Get the rectangle's width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for the optional width attribute """

        Rectangle.validate_attribute("width", value)
        self.__width = value

    @property
    def height(self):
        """ Get the rectangle's height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for the optional height attribute """

        Rectangle.validate_attribute("height", value)
        self.__height = value

    @property
    def x(self):
        """ Get the rectangle's x position """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter method for the x position attribute """

        Rectangle.validate_attribute("x", value)
        self.__x = value

    @property
    def y(self):
        """ Get the rectangle's y position """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter method for the y position attribute """

        Rectangle.validate_attribute("y", value)
        self.__y = value

    def area(self):
        """ This function returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """ This method prints the Rectangle with '#' chacarters
        considering the x and y positions
        """
        for ctr in range(self.y):
            print()
        for itr in range(self.__height):
            print(" " * self.x + '#' * self.__width)

    def __str__(self):
        """ This function returns the print(( and str() representation
        of the rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ This method updates the attributes using the no keyword
        and key worded arguments

        Args:
            *args: The variable number of the arguments in the order
                id, width, height, x, y
            **kwargss: The key worded arguments to update the attributes
        """
        if len(args) == 0:
            for attr, val in kwargs.items():
                self.__setattr__(attr, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """ This is the method representing the rectangle """
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }

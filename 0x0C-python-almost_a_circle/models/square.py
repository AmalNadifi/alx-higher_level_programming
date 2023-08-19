#!/usr/bin/python3
""" Definition of a Square class inherited from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class represents a Square  """

    def __init__(self, size, x=0, y=0, id=None):
        """ This method initializes a new square

        Args:
        size (int): The square's size
        x (int): The x position of the square
        y (int): The y position of the square
        id (int): The unique "id" of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Get the square's size """
        return self.__width

    @size.setter
    def size(self, value):
        """ Setter method for the optional width attribute """
        self.__width = value
        self.__height = value

    def __str__(self):
        """ This method returns the print() and str() representation
        of the square
        """
        return "[Squaree] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.__width)

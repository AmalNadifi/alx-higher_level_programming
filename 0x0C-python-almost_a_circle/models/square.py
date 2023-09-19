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
        return self.width

    @size.setter
    def size(self, value):
        """ Setter method for the optional width attribute """
        self.width = value
        self.height = value

    def __str__(self):
        """ This method returns the print() and str() representation
        of the square
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ This method updates the attributes using the no keyword
        and key worded arguments

        Args:
            *args: The variable number of the arguments in the order
            id, size, x, y
            **kwargs: The key worded arguments to update the attributes
        """
        if len(args) == 0:
            for attr, val in kwargs.items():
                self.__setattr__(attr, val)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """ This is the method representing the rectangle """
        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'size': self.size
                }

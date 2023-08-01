#!/usr/bin/python3
""" Definition of a class Square with size validation"""


class Square:
    """ This class represents a Square

    Attributes:
    __size (int): Size of the square as a private instance attribute
    """

    def __init__(self, size=0):
        """
        Initialization of the Square instance with an optional size

        Args:
            size (int, optional): The size of the square

        Raises:
            TypeError: If the given size is not an integer
            ValueError: If the given size is < 0
        """
        self.size = size

    @property
    def size(self):
        """ Getter method for the optional size attribute

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method for the optional size attribute

        Args:
            value (int): The integer value for the square size
        Raises:
            TypeError: if the given size is not an int
            ValueError: If the given size is < 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculation of the square area

        Returns:
            int: The square area
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        equality opeartor for the square area instances

        Args:
            other(Square): The second square to compare

        Returns:
            bool: True if (square areas are the same) or False (failure)
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        inequality opeartor for the square area instances

        Args:
            other(Square): The second square to compare

        Returns:
            bool: True if (square areas are not the same) or False (failure)
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        greater than opeartor for the square area instances

        Args:
            other(Square): The second square to compare

        Returns:
            bool: True if (area of square1 is greater than area of
            square2) or False (failure)
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        greater than or equal to 0 opeartor for the square area instances

        Args:
            other(Square): The second square to compare

        Returns:
            bool: True if (area of square1 >= area of square2)
            or False(failure)
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        less than opeartor for the square area instances

        Args:
            other(Square): The second square to compare

        Returns:
            bool: True if (area of square1 < area of square2)
            or False (failure)
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        less than or equal to 0 opeartor for the square area instances

        Args:
            other(Square): The second square to compare

        Returns:
            bool: True if (area of square1 <= area of square2)
            or False (failure)
        """
        return self.area() <= other.area()

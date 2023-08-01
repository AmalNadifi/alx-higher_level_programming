#!/usr/bin/python3
""" Definition of a class Square with size validation"""


class Square:
    """ This class represents a Square

    Attributes:
    __size (int): Size of the square as a private instance attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization of the Square instance with an optional size

        Args:
            size (int, optional): The size of the square
            position (tuple, optional): The square position x and y

        Raises:
            TypeError: If the given size is not an integer
            ValueError: If the given size is < 0
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Getter method for the position attribute

        Returns:
            tuple: the x and y as position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter method for the suqare position

        Args:
            value (tuple): the x and y as the suqare position
        Raises:
            TypeError: If value is not a tuple || value is not
            exactly 2 integers
            ValueError: If the given integers are not >= 0
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(numb, int) for numb in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if x < 0 or y < 0:
            raise ValueError("position must contain positive integers")
        self.__position = value

    def area(self):
        """ Calculation of the square area

        Returns:
            int: The square area
        """
        return self.__size ** 2

    def my_print(self):
        """ Printing the square using the '#' character

        if the square size is zero , it does print an empty line
        """
        if self.__size == 0:
            print()
        else:
            for itr in range(self.__position[1]):
                print()
            for itr in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)
    def __str__(self):
        """ This returns the square string representation

        Returns:
            str: The square string representation with the '#' character
        """
        sq_str = ""
        if self.__size == 0:
            sq_str = sq_str + "\n"
        else:
            for y in range(self.__position[1]):
                sq_str = sq_str + "\n"
            for count in range(self.__size):
                sq_str = sq_str + " " * self.__position[0] + '#' * self.__size
                + "\n"
        return sq_str.strip()

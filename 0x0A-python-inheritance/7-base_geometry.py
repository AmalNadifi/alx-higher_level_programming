#!/usr/bin/python3
""" Definition of a base geometry class BaseGeometry """


class BaseGeometry:
    """ This is representing the base geometry """

    def area(self):
        """ not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This function validates a parameter asan integer

        Args:
            name (str): the parameter name
            value (int): parameter to validate
        Raises:
            TypeError: If valueis not int
            ValueError: if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

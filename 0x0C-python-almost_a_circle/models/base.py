#!/usr/bin/python3
""" Definition of the base model class."""
import csv
import json
import turtle


class Base:
    """ This class represents the Base model for all the classes
    in project 0x0C Python

    Attributes:
        __no__objects (int): How many instantiated bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization of a new Base

        Args:
            id (int) : The new Base identity
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

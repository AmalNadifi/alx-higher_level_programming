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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This method returns the JSON string representation
        of a list of dictionaries

        Args:
            list_dictionaries (list): The list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ This method writes the JSON string representation
        of a list of instances who inherits of Base

        Args:
            list_objs (list): The list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        json_list = []

        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(json_list))

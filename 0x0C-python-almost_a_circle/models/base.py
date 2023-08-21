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

    @staticmethod
    def from_json_string(json_string):
        """ This method returns a list of the JSON string representation
        of a list of dictionaries

        Args:
            json_string (str): JSON string to convert to a list of dictionaries

        Returns:
            list: List of dictionaries represented by the JSON string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ This method returns an instance with all attributes already set

        Args:
            **dictionary: Keyword arguments representing the attributes

        Returns:
            object: The instance with attributes set using
            the provided dictionary
        """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ This method returns a list of instances loaded from
        a JSON file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_string = file.read()
                json_list = cls.from_json_string(json_string)
                instances = [cls.create(**item) for item in json_list]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ This method serializes and saves instances to CSV file

        Args:
            list_objs (list): The list of instances to be serialized
        """
        filename = cls.__name__ + ".csv"
        csv_rows = []

        if list_objs is not None:
            for obj in list_objs:
                csv_rows.append(obj.to_csv_row())
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            for row in csv_rows:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """ This method deserializes instances from CSV file

        Returns:
            list: The list of instances deserialized from the CSV file
        """
        filename = cls.__name__ + ".csv"
        instances = []

        try:
            with open(filename, mode="r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(
                                int(row[1]),
                                int(row[2]),
                                int(row[3]),
                                int(row[4]),
                                int(row[0])
                                )
                    elif cls.__name__ == "Square":
                        instance = cls(
                                int(row[1]),
                                int(row[2]),
                                int(row[3]),
                                int(row[0])
                                )
                    instances.append(instance)
            return instances
        except FileNotFoundError:
            return []

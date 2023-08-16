#!/usr/bin/python3
""" Definition of a class Student """


class Student:
    """ Representation of a student """

    def __init__(self, first_name, last_name, age):
        """ Initilization of a new Student

        Args:
            first_name (str): the student first name
            last_name (str): the student last name
            age (int): the student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ the public method retrieves a dictionary representation
        of a Student instance """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ The function replaces all attributes of the Student instance"""
        for k, v in json.items():
            setattr(self, k, v)

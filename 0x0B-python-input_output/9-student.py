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

    def to_json(self):
        """ the public method retrieves a dictionary representation
        of a Student instance """
        return self.__dict__

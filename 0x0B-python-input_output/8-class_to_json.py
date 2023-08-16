#!/usr/bin/python3
""" Definition of a function python class to JSON """


def class_to_join(obj):
    """ This function returns the the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object"""
    return obj.__dict__

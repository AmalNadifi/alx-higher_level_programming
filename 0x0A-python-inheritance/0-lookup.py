#!/usr/bin/python3
""" Definition of a lookup function for object attribute """


def lookup(obj):
    """ This function returns a list containing the names of attributes
    and methods of the object
    """
    return (dir(obj))

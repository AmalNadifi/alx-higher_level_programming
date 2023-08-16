#!/usr/bin/python3
""" Definition of a function for class checking """


def is_same_class(obj, a_class):
    """ This function checks if the object is exactly an instance
    of the specified class.

    Args:
        obj: Object to check
        a_class: the class to compare the object class with

    Returns:
        True: if the objects class is exactly the same as the specified class
        False: otherwise
    """
    return type(obj) is a_class

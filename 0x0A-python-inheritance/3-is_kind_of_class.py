#!/usr/bin/python3
""" Definition of a function for class and inherited class checking """


def is_kind_of_class(obj, a_class):
    """ This function checks if the object is exactly an instance
    or inherited instance of the specified class.

     Args:
        obj: Object to check
        a_class: the class to compare the object class with

    Returns:
        True: if the objects class is an instance of as the specified class
            or a subclass of it
        False: otherwise
    """
    return isinstance(obj, a_class)

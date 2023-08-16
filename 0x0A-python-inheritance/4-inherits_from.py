#!/usr/bin/python3
""" Definition of a function for inherited class checking """


def inherited_from(obj, a_class):
    """ This function checks if The object is an instance of a class
    that inherited directly or indirectly from the specified class.

    Args:
        obj: Object to check
        a_class: the class to compare the object class with

    Returns:
        True: if the objects class is a subclass of a the specified class
        False: otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

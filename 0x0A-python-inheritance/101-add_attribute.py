#!/usr/bin/python3
""" Definition of a function that is adding new attributes to objects """


def add_attribute(obj, attr_name, attr_value):
    """ This function adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute will be added
        attr_name: The name of the attribute to add
        attr_value: The value of the attribute to add

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)

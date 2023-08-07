#!/usr/bin/python3
""" Definition of a module to print first and last name """


def say_my_name(first_name, last_name=""):
    """ Printing first and last name

    Args:
        first_name (str): The first name in the name
        last_name (str, optional): The last name in the name

    Raises:
        TypeError: if first or last name is not string

    Returns:
        None
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = "My name is {} {}".format(first_name, last_name)
    print(full_name)

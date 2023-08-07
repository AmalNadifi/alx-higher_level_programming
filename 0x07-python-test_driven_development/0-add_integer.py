#!/usr/bin/python3
def add_integer(a, b=98):
    """ Definition of a function adding 2 integers

    Args:
        a (int or float): The first number to add
        b (int or float): The second number to be added

    Returns:
        int: The resultant sum of 'a' and 'b' after being converted to inegers

    Raises:
        TypeError: If 'a' or 'b' is not an int or float
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)

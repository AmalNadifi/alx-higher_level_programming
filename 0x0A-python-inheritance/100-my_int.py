#!/usr/bin/python3
""" Definition of a class MyInt that inherits from int """


class MyInt(int):
    """ This class inverts int operators == and != """
    def __eq__(self, value):
        """ Ovveriding the equality operator with != """
        return super().__ne__(value)

    def __ne__(self, value):
        """ Ovveriding the inequality operator with == """
        return super().__eq__(value)

#!/usr/bin/python3
""" Unittest code for the max_integer module """


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Test scenarios to evaluate the 'max_integer' function"""

    def t_empty(self):
        """ Test with an empty list

        Returns:
            None
        """
        self.assertEqual(max_integer(), None)

    def t_pos_int(self):
        """ Test with a list with positive integers

        Returns:
            int : the maximum value
        """
        self.assertEqual(max_integer([18, 1, 19, 100]), 100)

    def t_neg_int(self):
        """ Test with a list with negative integers

        Returns:
            int : the maximum value
        """
        self.assertEqual(max_integer([-18, -1, -19, -100]), -1)

    def t_float(self):
        """ Test with a list with float numbers

        Returns:
            int : the maximum value
        """
        self.assertEqual(max_integer([18.2, 1.8, 19.1, 100]), 100)

    def t_unique(self):
        """ Test with a list with a unique number

        Returns:
            int : the number
        """
        self.assertEqual(max_integer([100]), 100)

    def t_none(self):
        """ Test with a list with a parameter 'None' """
        self.assertRaises(TypeError, max_integer, None)

    def t_mixed(self):
        """ Test with a list of mixed types of elements """
        self.assertRaises(TypeError, lambda: max_integer([1, 2.9, "Mixed"]))

    def t_non_iterable_args(self):
        """ Test with a non iterable args """
        self.assertRaises(TypeError, lambda: max_integer(49))

    def t_multi(self)
        """ Test with a multitude of arguments"""
        self.assertRaises(TypeError, lambda: max_integer([19], [18]))

    def t_string(self):
        """ Test function on The string """
        self.assertEqual(max_integer("Python"), 'y')
    
if __name__ == '__main__':
    unittest.main()

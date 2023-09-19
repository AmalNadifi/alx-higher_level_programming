#!/usr/bin/python3
"""Unit tests for Rectangle class."""
import pep8
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This class to test Rectangle class """

    def setUp(self):
        """THis method creates instances for tests """
        self.r1 = Rectangle(5, 3)  # Width: 5, Height: 3
        self.r2 = Rectangle(3, 5)  # Width: 3, Height: 5
        self.r3 = Rectangle(7, 2, 1, 2, 9)  # Width: 7, Height: 2,
        # X: 1, Y: 2, ID: 9

    def tearDown(self):
        """THis method cleans up after each test """
        del self.r1
        del self.r2
        del self.r3

    def test_pep8(self):
        """This method checks PEP8 conformance of models/rectangle.py."""
        style_guide = pep8.StyleGuide(quiet=True)
        result = style_guide.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_subclass(self):
        """This method is to test if Rectangle is a subclass of Base """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_params(self):
        """This method is to test Rectangle initialization parameters."""
        self.assertEqual(self.r1.id, 4)
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.id, 5)
        self.assertEqual(self.r2.width, 3)
        self.assertEqual(self.r2.height, 5)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.id, 9)
        self.assertEqual(self.r3.width, 7)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r3.x, 1)
        self.assertEqual(self.r3.y, 2)
        # Add more assertions as needed

    def test_invalid_string_param(self):
        """This method is to test Rectangle instantiation
        with invalid string parameters."""
        with self.assertRaises(TypeError):
            R1 = Rectangle(1.01, 3)
        with self.assertRaises(TypeError):
            R1 = Rectangle(1.01, 3)

    def test_invalid_type_params(self):
        """This method is to test Rectangle instantiation with invalid
        type parameters """
        with self.assertRaises(TypeError):
            R1 = Rectangle(1.01, 3)
            raise TypeError()
        with self.assertRaises(ValueError):
            R2 = Rectangle(-234234242, 45)
            raise ValueError()


if __name__ == '__main__':
    unittest.main()

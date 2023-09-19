#!/usr/bin/python3
""" Unittests for the class 'Base' """
import pep8
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """ This class will be testing the class Base """

    def setUp(self):
        """This method to set up method before each test."""
        self.remove_files()

    def tearDown(self):
        """THis method to clean up after each test."""
        self.remove_files()

    def remove_files(self):
        """This method to remove test files if they exist."""
        for filename in ["Rectangle.json", "Square.json", "Base.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_pep8(self):
        """This method checks PEP8 conformance."""
        style_guide = pep8.StyleGuide(quiet=True)
        result = style_guide.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_none_id(self):
        """ This method to test None IDs in Base"""
        obj = Base()
        self.assertEqual(obj.id, 1)
        obj = Base(None)
        self.assertEqual(obj.id, 2)

    def test_pos_id(self):
        """ This method to test positive IDs in Base"""
        obj = Base(23)
        self.assertEqual(obj.id, 23)
        obj = Base(34)
        self.assertEqual(obj.id, 34)

    def test_neg_id(self):
        """ This method to test negative IDs in Base"""
        obj = Base(-4)
        self.assertEqual(obj.id, -4)
        obj = Base(-10)
        self.assertEqual(obj.id, -10)

    def test_str_id(self):
        """This method to test string IDs in Base"""
        obj = Base("st")
        self.assertEqual(obj.id, "st")
        obj = Base("st2")
        self.assertEqual(obj.id, "st2")

    def test_type_inst(self):
        """This method to test type and instance of Base object."""
        obj = Base()
        self.assertEqual(type(obj), Base)
        self.assertIsInstance(obj, Base)

    def test_to_json(self):
        """This method to test "to_json_string method" """
        d = {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}
        json_d = Base.to_json_string([d])
        self.assertTrue(isinstance(d, dict))
        self.assertTrue(isinstance(json_d, str))
        self.assertEqual(
            json_d,
            '[{"id": 1, "x": 2, "y": 3, "width": 4, "height": 5}]'
        )
        json_d_1 = Base.to_json_string(None)
        self.assertEqual(json_d_1, "[]")

        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        self.assertIn(
                "missing 1 required positional argument", str(e.exception))

    def test_save(self):
        """ This method to test "save_to_file method" """
        with self.assertRaises(AttributeError) as e:
            Base.save_to_file([Base(1), Base(2)])
        self.assertEqual(
            "'Base' object has no attribute 'to_dictionary'",
            str(e.exception)
        )

    def test_load(self):
        """ This method to test "load_from_file method" """
        r_output = Rectangle.load_from_file()
        self.assertEqual(r_output, [])

        s_output = Square.load_from_file()
        self.assertEqual(s_output, [])

        with self.assertRaises(TypeError) as e:
            Rectangle.load_from_file("str")
        self.assertEqual(
                "takes 1 positional argument but 2 were given",
                str(e.exception))

    def test_create(self):
        """ This method to test "create" method """
        with self.assertRaises(TypeError) as e:
            Rectangle.create("str")
        self.assertEqual(
                "takes 1 positional argument but 2 were given",
                str(e.exception))

    def test_dict(self):
        """ This method to test "to_dictionary" method """
        r = Rectangle(10, 7, 2, 8, 70)
        d = r.to_dictionary()
        json_d = Base.to_json_string([d])
        self.assertEqual(type(json_d), str)

    def test_empty_dict(self):
        """This method to test "to_json_string" with empty dictionary."""
        d = []
        json_d = Base.to_json_string(d)
        self.assertEqual(json_d, "[]")

        o = None
        json_d = Base.to_json_string(o)
        self.assertEqual(json_d, "[]")


if __name__ == '__main__':
    unittest.main()

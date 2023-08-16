#!/usr/bin/python3
""" Definition of a function that writes an object to a text file,
using the JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """ This is the function that writes an object to a text file
    using JSON representation """
    with open(filename, "w") as f:
        json.dump(my_obj, f)

#!/usr/bin/python3
""" Definition of a function creating an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """ This is the function that creates a python object from JSON file"""
    with open(filename) as f:
        return json.load(f)

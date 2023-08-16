#!/usr/bin/python3
""" Definition of a function returning the JSON representation
of an object (string) """
import json


def to_json_string(my_obj):
    """ This function the JSON representationof an object (string) """
    return json.dumps(my_obj)

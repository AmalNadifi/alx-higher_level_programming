#!/usr/bin/python3
""" Definition of a function returning an object(Python data structure)
represented by a JSON string"""
import json


def from_json_string(my_str):
    """ This is the json-to_string function"""
    return json.loads(my_str)

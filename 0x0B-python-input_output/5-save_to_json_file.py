#!/usr/bin/python3
""" Module that writes an Object to a text file using
a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an object to a text file
    by a JSON representation
    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, 'w', encoding="UTF-8") as fi:
        json.dump(my_obj, fi)

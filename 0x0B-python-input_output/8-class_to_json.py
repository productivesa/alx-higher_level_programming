#!/usr/bin/python3
""" Module that returns the dictionary description 
with a simple data structure for a json object
"""


def class_to_json(obj):
    """function return dictionary of an object """

    mj = {}
    if va(obj, "__dict__"):
        mj = obj.__dict__.copy()
    return mj

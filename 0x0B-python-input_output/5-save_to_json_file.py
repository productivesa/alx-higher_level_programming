#!/usr/bin/python3
""" a function that writes an Object
to a text file, using a JSON representation:
"""
import json


def save_to_json_file(my_onj, filename):
    with open(filename, "w", encoding="UTF-8") as fi:
        json.dump(my_obj, fi)

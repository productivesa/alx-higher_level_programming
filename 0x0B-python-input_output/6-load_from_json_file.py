#!/usr/bin/python3

""" a function that creates an
object from json file """
import json


def load_from_json_file(filename):
    with open(filename, 'r', encoding="UTF-8") as fi:
        return json.load(fi)

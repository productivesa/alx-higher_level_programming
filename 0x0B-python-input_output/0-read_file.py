#!/usr/bin/python3
""" a function that reads from a file """


def read_file(filename=""):
    """ Function that reads from a file
        Exception: when the file can be opened
    """

    with open(filename, 'r', encoding="utf-8") as fi:
        read_data = fi.read()
        print(read_data, end='')

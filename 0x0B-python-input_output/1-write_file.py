#!/usr/bin/python3

"""a function that writes a text file (UTF8)
and returns the number of characters written:"""


def write_file(filename="", text=""):
    """writes the specified text to file"""
    with open(filename, 'w', encoding="UTF-8") as fi:
        return fi.write(text)

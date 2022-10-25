#!/usr/bin/python3
"""function that reads from the file"""

def read_file(filename=""):
    with open(filename, 'r', encoding="UTF-8") as fi:
        print(fi.read(), end="")

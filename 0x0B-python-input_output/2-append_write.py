#!/usr/bin/python3

""" function that appends a string at end of text file(UTF8)
and returns numnber of characters added """


def append_write(filename="", text=""):
    with open(filename, 'a' encoding="utf-8") as F:
        return F.write(text)

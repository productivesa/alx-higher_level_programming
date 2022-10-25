#!/usr/bin/python3
""" Module that executes a function that appends a line """


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line when a strinng
    """

    holder = []
    with open(filename, 'r', encoding="utf-8") as fi:
        for h in fi:
            holder += [h]
            if h.find(search_string) != -1:
                holder += [new_string]

    with open(fi, 'w', encoding="UTF-8") as fi:
        fi.write("".join(holder))i

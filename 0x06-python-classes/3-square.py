#!/usr/bin/python3

"""a class Square that defines a
square by: (based on 2-square.py)"""


class Square:
    def __init__(self, size=0):
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size * self.__size

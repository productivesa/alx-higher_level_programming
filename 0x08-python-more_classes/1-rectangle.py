#!/usr/bin/python3
"""A class that defines a Rectangle"""


class Rectangle:
    """
    Rectangle (class): creates a rectangle with the size specified by
    the parameter height and width

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width should be an integer")
        else:
            if value < 0:
                raise ValueError("width should be >= 0")
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height should be an integer")
        else:
            if value < 0:
                raise ValueError("height should be >= 0")
            self.__height = value

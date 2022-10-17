#!/usr/bin/python3
""" a class that defines a rectangle based on 0-rectangle.py"""


class Rectangle:
    """
    (class) Rectangle: it creates a rectangle with size specified by
    parameter height and width

    Attributes:
    width: width of rectangle
    height: height of rectangle
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
            raise TypeError("width must be integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height should be integer")
        else:
            if value < 0:
                raise TypeError("height should >= 0")
            self.__height = value



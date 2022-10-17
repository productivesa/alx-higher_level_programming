#!/usr/bin/python3
"""A class that really defines a Rectangle"""


class Rectangle:
    """
    Rectangle (class): creates a rectangle with the size specified by
    the parameter height and width
    Attributes:
        width (int): specify the width of the rectangle.
        height (int): specifies the height of the rectangle
    Args:
        Area: returns the area of the rectangle
        Perimeter: returns the perimeter of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

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

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(0, self.__height):
            [print("#", end="") for j in range(0, self.__width)]
            if i != self.__height - 1:
                print("")
        return ""

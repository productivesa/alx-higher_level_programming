#!/usr/bin/python3
""" Module defines class student """


class Student:
    """ creating student classs """

    def __init__(self, first_name, last_name, age):
        self.firstname = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__.copy()

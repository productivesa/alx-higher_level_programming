#!/usr/bin/python3
def print_last_digit(number):
    last_degit = abs(number) % 10
    print("{}".format(last_degit), end='')
    return last_degit

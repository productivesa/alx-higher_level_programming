#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    x = 0
    len = 0
    for y in my_list:
        x += (y[0] * y[1])
        len += y[1]
    return (x / len)

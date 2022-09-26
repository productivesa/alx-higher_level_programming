#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a == 0:
        x = 0
        x1 = 0
    elif len_a == 1:
        x = tuple_a[0]
        x1 = 0
    else:
        x = tuple_a[0]
        x1 = tuple_a[1]

    if len_b == 0:
        y = 0
        y1 = 0
    elif len_b == 1:
        y = tuple_b[0]
        y1 = 0
    else:
        y = tuple_b[0]
        y1 = tuple_b[1]

    new_tuple = (x + y, x1 + y1)

    return (new_tuple)

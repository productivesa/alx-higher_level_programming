#!/usr/bin/python3
def uniq_add(my_list=[]):
    empty = []
    total = 0
    for x in my_list:
        if x not in empty:
            empty.append(int(x))
            total += x
    return total

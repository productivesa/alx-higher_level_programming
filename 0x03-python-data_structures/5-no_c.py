#!/usr/bin/python3
def no_c(my_string):
    removed_string = ''
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        removed_string = removed_string + char
    return removed_string

#!/usr/bin/python3

"""a function that prints the first x
elements of a list and only integers."""


def safe_print_list_integers(my_list=[], x=0):
    lister = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end='')
            lister += 1
        except (ValueError, TypeError):
            continue
    print('')
    return lister

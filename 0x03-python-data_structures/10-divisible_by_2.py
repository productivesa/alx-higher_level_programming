#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = []
    for x in my_list:
        if (x % 2):
            list_result.append(False)
        else:
            list_result.append(True)
    return list_result

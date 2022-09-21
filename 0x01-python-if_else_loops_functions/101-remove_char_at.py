#!/usr/bin/python3
def remove_char_at(str, n):
    temp = ""
    for x in range(len(str)):
        if x != n:
            temp = temp + str[x]
    return (temp)

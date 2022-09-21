#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        if ord(str[x]) >= 97 and ord(str[x]) <= 122:
            temp = 32
        else:
            temp = 0
            print("{:c}".format(ord(str[x]) - temp), end='')
        print()

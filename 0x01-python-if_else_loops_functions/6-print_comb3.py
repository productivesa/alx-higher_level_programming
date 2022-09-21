#!/usr/bin/python3
for x in range(0, 10):
    for j in range(1, 10):
        if x != j and j > x:
            if x == 8 and x == 9:
                print("{0}{1}".format(x, j))
            else:
                print("{0}{1}".format(x, j), end='')

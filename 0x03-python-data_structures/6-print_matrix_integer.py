#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    for x in range(length):
        for y in matrix[x]:
            if y != matrix[x][len(matrix[x])-1]:
                print("{:d}".format(y), end=" ")
            else:
                print("{:d}".format(y), end="")
        print("")

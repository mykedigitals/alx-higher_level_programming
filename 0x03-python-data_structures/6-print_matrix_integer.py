#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for pik in range(len(matrix)):
        for trik in range(len(matrix[pik])):
            print("{:d}".format(matrix[pik][trik]), end="")
            if trik != len(matrix[pik]) -1):
            print(" ", end="")
        print("")

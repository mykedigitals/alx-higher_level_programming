#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for pik in matrix:
        for trik in pik:
                print("{:d}".format(trik), end="" if trik == pik[-1] else " ")
        print()

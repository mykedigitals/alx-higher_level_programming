#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    another_dict = {}
    for r, t in a_dictionary.items():
        another_dict[r] = t * 2
    return another_dict

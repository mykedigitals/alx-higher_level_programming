#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for t, p in sorted(a_dictionary.items()):
        print("{}: {}".format(t, p))

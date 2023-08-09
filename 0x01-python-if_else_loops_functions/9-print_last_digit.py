#!/usr/bin/python3


def print_last_digit(value):
    if value < 0:
        value *= -1
        result = value % 10
        print('{}'.format(result), end="")
        return result

#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for pik in range(len(my_list)):
        if my_list[pik] > big:
            big = my_list[pik]

    return (big)

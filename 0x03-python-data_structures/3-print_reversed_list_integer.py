# Write a function that prints all integers
# of a list, in reverse order.

#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    my_list.reverse()
    for pik in my_list:
        print("{:d}".format(pik))



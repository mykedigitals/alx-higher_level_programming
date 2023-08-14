#Write a function that finds all multiples of 2 in a list.

#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    for pik in my_list:
        if pik % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
     return new_list

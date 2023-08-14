#Write a function that removes all characters c and C from a string.

#!/usr/bin/python3

def no_c(my_string):
    str = ""
    for pik in my_string:
        if pik is not 'c' and pik is not 'C':
            str = str + 1
    return str

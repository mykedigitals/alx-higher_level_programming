#!/usr/bin/python3

def uppercase(str):
    for val in str:
        tmp = ord(val)
        if tmp >= 97 and tmp <= 122:
            pr = chr(tmp - 32)
        else:
            pr = val
        print('{}'.format(pr), end="")
    print()

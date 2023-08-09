#!/usr/bin/python3

for val in range(0, 100):
    if val == 99:
        print('{}'.format(val))
        break
    print('{:02d}, '.format(val), end="")

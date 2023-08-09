#!/usr/bin/python3

for val in range(0, 10):
    for num in range(0, 10):
        if val >= num:
            continue
        elif val == 8 and num == 9:
            print('{}{}'.format(val, num))
        else:
            print('{}{}, '.format(val, num), end="")

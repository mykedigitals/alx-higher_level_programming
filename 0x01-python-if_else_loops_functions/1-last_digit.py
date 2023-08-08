#!/usr/bin/python3
import random
val = random.randint(-10000, 10000)
amt = abs(val) % 10

if val < 0:
    amt = -amt
    print("Last amt of {} is {} and is ".format(val, amt), end="")
    if amt > 5:
        print("greater than 5")
    elif amt == 0:
        print("0")
    else:
        print("less than 6 and not 0")

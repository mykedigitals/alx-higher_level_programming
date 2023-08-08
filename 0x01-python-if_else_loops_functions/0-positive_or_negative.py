#!/usr/bin/python3

import random
val = random.randint(-10, 10)

if val > 0:
    print("{} is positive".format(val))
elif val < 0:
    print("{} is negative".format(val))
elif val == 0:
    print("{} is zero".format(val))

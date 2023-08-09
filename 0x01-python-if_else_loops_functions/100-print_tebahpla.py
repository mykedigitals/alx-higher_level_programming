#!/usr/bin/python3

""""Print the alphabet in reverse order alternating upper- and lower-case."""

val = 0
for num in range(ord('z'), ord('a') - 1, -1):
        print("{}".format(chr(num - val)), end="")
        val = 32 if val == 0 else 0

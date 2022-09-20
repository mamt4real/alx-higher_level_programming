#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if number < 0:
    ld *= -1
fmt = f"Last digit of {number:d} is {ld:d} and is"
if ld > 5:
    print(f"{fmt:s} greater than 5")
elif ld == 0:
    print(f"{fmt:s} 0")
else:
    print(f"{fmt:s} less than 6 and not 0")

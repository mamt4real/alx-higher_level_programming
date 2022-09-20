#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
fmt = f"The last digit of {number:d} is {ld:d} and is"
if ld > 5:
    print(f"{fmt:s} greater than 5")
elif ld == 0:
    print(f"{fmt:s} 0")
else:
    print(f"{fmt:s} less than 6 and not 0")

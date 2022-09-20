#!/usr/bin/python3

def uppercase(s):
    """prints a string in uppercase"""
    lower = range(97, 97 + 26)
    for c in s:
        i = ord(c)
        if i in lower:
            i -= 32
        print("{n:c}".format(n=i), end='')
    print()


if __name__ == '__main__':
    uppercase('some856lowercase₦&@')

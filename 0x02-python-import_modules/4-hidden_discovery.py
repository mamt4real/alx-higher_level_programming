#!/usr/bin/python3
import hidden_4 as h

if __name__ == '__main__':
    names = filter(lambda n: not n.startswith('_'), dir(h))
    print("\n".join(names))

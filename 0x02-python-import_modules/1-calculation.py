#!/usr/bin/python3
import calculator_1 as cacl

if __name__ == '__main__':
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, cacl.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, cacl.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, cacl.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, cacl.div(a, b)))

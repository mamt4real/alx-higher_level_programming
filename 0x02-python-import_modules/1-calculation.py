#!/usr/bin/python3
import calculator_1 as calc

if __name__ == '__main__':
    a = 10
    b = 5
    funcs = (calc.add, calc.sub, calc.mul, calc.div)
    for op, func in zip('+-*/', funcs):
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, func(a, b)))

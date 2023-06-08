#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b =5
    result = (add(a, b), sub(a, b), mul(a, b), div(a, b))
    print("{} + {} = {}".format(a, b, result[0]))
    print("{} - {} = {}".format(a, b, result[1]))
    print("{} * {} = {}".format(a, b, result[2]))
    print("{} / {} = {}".format(a, b, result[3]))

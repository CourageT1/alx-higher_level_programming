#!/usr/bin/python3
for k in range(0, 10):
    for i in range(k + 1, 10):
        if k == 8 and i == 9:
            print("{}{}".format(k, i))
        else:
            print("{}{}".format(k, i), end=", ")

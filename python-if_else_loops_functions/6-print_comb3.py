#!/usr/bin/python3
for i in range(10):
    for a in range(i + 1, 10):
        if i * 10 + a < 89:
            print("{:02d}".format(i * 10 + a), end=", ")
        else:
            print("{:02d}".format(i * 10 + a))

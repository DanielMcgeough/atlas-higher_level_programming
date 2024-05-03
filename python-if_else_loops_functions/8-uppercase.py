#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (ord(c) >= ord('a') and ord(c) <= ('z')):
            char = chr(ord(c) - 32)
        else:
            char = c
        print("{}".format(char), end='')
    print()

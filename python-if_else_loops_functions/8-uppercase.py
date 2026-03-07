#!/usr/bin/python3
def uppercase(str):
    for i in str:
        char = i
        if ord(i) > 96 and ord(i) < 124:
            char = chr(ord(i) - 32)
        print("{}".format(char), end="")
    print()

#!/usr/bin/python3
import sys
if __name__ == "__main__":
    len_argv = len(sys.argv)
    if len_argv == 1:
        print("0 arguments.")
    elif len_argv == 2:
        print("{} argument:".format(len_argv - 1))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len_argv - 1))
        for i in range(1, len_argv):
            print("{}: {}".format(i, sys.argv[i]))

#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)

    if argc == 1:
        print("0 arguments.")
    else:
        if argc == 2:
            print("{:d} argument:".format(argc - 1))
        else:
            print("{:d} arguments:".format(argc - 1))

        for i in range(1, argc):
            print("{:d}: {}".format(i, argv[i]))

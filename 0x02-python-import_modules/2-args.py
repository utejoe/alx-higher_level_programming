#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    no_of_args = len(sys.argv) - 1
    if no_of_args == 1:
        print("{:d} argument:".format(no_of_args))
    elif no_of_args == 0:
        print("{:d} arguments.".format(no_of_args))
    elif int(no_of_args) > 1:
        print("{:d} arguments:".format(no_of_args))

    if int(no_of_args) >= 1:
        for i in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(i, sys.argv[i]))

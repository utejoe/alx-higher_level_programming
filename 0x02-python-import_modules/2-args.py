#!/usr/bin/python3
import sys

args = sys.argv
num_args = len(args) - 1

if num_args == 0:
    print("0 arguments.")
else:
    print("{} argument{}:".format(num_args, "" if num_args == 1 else "s"))
    for i in range(1, len(args)):
        print("{}: {}".format(i, args[i]))
#!/usr/bin/python3
import sys

args = sys.argv[1:]
count = len(args)

if count == 0:
    print("{:d} arguments.".format(count))
else:
    print("{:d} argument{}:".format(count, "" if count == 1 else "s"))
    for i, arg in enumerate(args):
        print("{:d}: {}".format(i+1, arg))

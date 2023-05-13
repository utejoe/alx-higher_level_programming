#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    len_args = len(sys.argv) - 1

    if len_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        if operator == '+':
            print("{} + {} = {:d}".format(a, b, add(a, b)))
            exit(0)
        elif operator == '-':
            print("{} - {} = {:d}".format(a, b, sub(a, b)))
            exit(0)
        elif operator == '*':
            print("{} * {} = {:d}".format(a, b, mul(a, b)))
            exit(0)
        elif operator == '/':
            print("{} / {} = {:d}".format(a, b, div(a, b)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    argc = len(sys.argv)
    result = 0
    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if sys.argv[2] != '+' and sys.argv[2] != '-' and sys.argv[2] != '*' and\
       sys.argv[2] != '/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    if sys.argv[2] == '+':
        result = add(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '-':
        result = sub(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '*':
        result = mul(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '/':
        result = div(int(sys.argv[1]), int(sys.argv[3]))
    print('{:d} {} {:d} = {:d}'.format(int(sys.argv[1]), sys.argv[2],
                                       int(sys.argv[3]), result))

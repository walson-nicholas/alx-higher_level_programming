#!/usr/bin/python3
<<<<<<< HEAD

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
=======
def main(argv):
    argc = len(argv)
    ops = {
        '+': calculator_1.add,
        '-': calculator_1.sub,
        '*': calculator_1.mul,
        '/': calculator_1.div,
    }
    if argc != 4:
        print('Usage: {:s} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op not in '+-*/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    res = ops[op](a, b)
    print('{:d} {:s} {:d} = {:d}'.format(a, op, b, res))


if __name__ == '__main__':
    from sys import argv, exit
    import calculator_1
    main(argv)
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3

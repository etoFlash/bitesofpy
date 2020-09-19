import argparse
from operator import add, sub, mul, truediv
from functools import reduce


def calculator(operation, numbers):
    """Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    if not numbers:
        raise SystemExit

    operator = {'add': add,
                'sub': sub,
                'mul': mul,
                'div': truediv,
                }

    return round(reduce(operator[operation], map(float, numbers)), 2)


def create_parser():
    """Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    parser = argparse.ArgumentParser('A simple calculator')
    parser.add_argument('-a', '--add', nargs='*', help='Sums numbers')
    parser.add_argument('-s', '--sub', nargs='*', help='Subtracts numbers')
    parser.add_argument('-m', '--mul', nargs='*', help='Multiplies numbers')
    parser.add_argument('-d', '--div', nargs='*', help='Divides numbers')

    return parser


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    print(args)
    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    call_calculator(stdout=True)

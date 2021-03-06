"""Print nth fibonacci number."""

import argparse
from itertools import islice


def get_args():
    """Get the users arguments."""
    parser = argparse.ArgumentParser('app')
    parser.add_argument('n', type=int)
    return parser.parse_args()


def fibo():
    """Calculate the fibonacci sequence."""
    x, y = 0, 1
    while True:
        x, y = y, x + y
        yield x


def main(n=0):
    """Run main program."""
    # Slice generator, pick first result
    g = fibo()
    subset = islice(g, n, None)
    result = next(subset)

    # Finally we print the result
    print(f'Fibonacci number {n} is {result}')


def cli():
    """Allow console script input (setup.py)."""
    n = get_args().n
    main(n)


if __name__ == "__main__":
    n = get_args().n
    main(n)

"""Itertools module"""
from typing import Iterable
import doctest


def count(start=0, step=1):
    while True:
        start += step
        yield start


def cycle(iterable):
    pass

def repeat(value, amount=None):
    if amount is None:
        while True:
            yield value
    else:
        for _ in range(amount):
            yield value


def product(*args: Iterable, repeat=1):
    """Product
    Returns cartesian product of input iterables
    Receives as a parameter an array of data, consisting of several groups of values.
    This product function allows you to get a new set of groups in all possible variations
    from an entered sequence of numbers or characters.

    To compute the product of an iterable with itself,
    specify the number of repetitions with the optional 'repeat' keyword argument.
    For example, product(A, repeat=4) means the same as product(A, A, A, A).

    The following examples shows the execution of this function and result in list format.
    >>> list(product('ABC', '123'))
    [('A', '1'), ('A', '2'), ('A', '3'), ('B', '1'), \
('B', '2'), ('B', '3'), ('C', '1'), ('C', '2'), ('C', '3')]
    >>> list(product('12', repeat=2))
    [('1', '1'), ('1', '2'), ('2', '1'), ('2', '2')]
    >>> list(product(repeat=10))
    [()]
    """
    # Function works recursively
    if not args:
        # Base case. If args iterator is empty - return ()
        yield tuple()
    else:
        # Include repeat case
        args *= repeat
        # Choose starting point
        element = args[0]
        # Iterate through elements in order to create combinations
        for item in element if callable(element) else iter(element):
            # 
            for elements in product(*args[1:]):
                yield (item, ) + elements


def permutations(iterable, length=None):
    pass


def combinations(r, n):
    pass


def combinations_with_replacement(r, n):
    pass


def main():
    pass


if __name__ == '__main__':
    main()

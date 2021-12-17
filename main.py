"""Itertools module"""
from typing import Iterable


def count(start=0, step=1):
    while True:
        start += step
        yield start


def cycle(iterable):
    pass

class repeat:
    """repeat
    Repeat(object [,times]) -> create an iterator which returns the object for the specified number of times.
    If 'amount' is not specified, returns the object endlessly

    The following examples shows the execution and result in list format.
    >>> list(repeat(10, 7))
    [10, 10, 10, 10, 10, 10, 10]
    >>> list(repeat(5, 1))
    [5]
    """
    def __init__(self, value, amount=None):
        self.value = value
        self.amount = amount
    def __iter__(self):
        if self.amount is None:
            while True:
                yield self.value
        else:
            for _ in range(self.amount):
                yield self.value
    def __str__(self):
        return f"repeat({self.value}, {self.amount if self.amount is not None else 'inf'})"


class product:
    """Product
    Returns cartesian product of input iterables
    Receives as a parameter an array of data, consisting of several groups of values.
    This product function allows you to get a new set of groups in all possible variations
    from an entered sequence of numbers or characters.

    To compute the product of an iterable with itself,
    specify the number of repetitions with the optional 'repeat' keyword argument.
    For example, product(A, repeat=4) means the same as product(A, A, A, A).

    The following examples shows the execution and result in list format.
    >>> list(product('ABC', '123'))
    [('A', '1'), ('A', '2'), ('A', '3'), ('B', '1'), \
('B', '2'), ('B', '3'), ('C', '1'), ('C', '2'), ('C', '3')]
    >>> list(product('12', repeat=2))
    [('1', '1'), ('1', '2'), ('2', '1'), ('2', '2')]
    >>> list(product(repeat=10))
    [()]
    """
    def __init__(self, *args, repeat=1):
        self.args = args
        self.repeat = repeat
    def __iter__(self):
        # Function works recursively
        if not self.args:
            # Base case. If args iterator is empty - return ()
            yield tuple()
        else:
            # Include repeat case
            self.args *= self.repeat
            # Choose starting point
            element = self.args[0]
            # Iterate through elements in order to create combinations
            for item in element if callable(element) else iter(element):
                # 
                for elements in product(*self.args[1:]):
                    yield (item, ) + elements
    def __str__(self):
        return f"Product(args: {self.args}, repeat={self.repeat})"


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
"""Itertools module"""

from typing import Iterable


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


def product(*iterables):
    pass


def permutations(iterable, length=None):
    pass


def combinations(r, n):
    pass


def combinations_with_replacement(iterable: Iterable, r: int):
    """ Combinations with replacement
    Return successive r-length combinations of elements in the iterable
    allowing individual elements to have successive repeats.

    The combination tuples are emitted in lexicographic ordering
    according to the order of the input iterable.
    Elements are treated as unique based on their position, not on their value.

    :param iterable: Iterable to iterate through, for instance 'ABC'
    :type iterable: Iterable
    :param r: length subsequences of elements
    :type r: int

    >>> list(combinations_with_replacement('ABC', 2))
    [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
    >>> list(combinations_with_replacement('ABC', 0))
    [()]
    >>> list(combinations_with_replacement('', 10))
    []
    """
    iterable_elements = tuple(iterable)  # Converting an iterable to tuple to increase program speed
    iterable_elements_len = len(iterable_elements) - 1  # Numeration in Python starts from 0

    if r < 0:
        # r must be non-negative, else stopping the program
        raise ValueError('r must be non-negative')

    if iterable_elements_len == -1:
        # If pool is empty then stop the program
        return None

    if r == 0:
        # Yield one empty tuple to reproduce default itertools behaviour if r == 0
        yield ()

    indices = [0 for _ in range(r - 1)] + [-1]  # initial indices setup
    # (zeroes and the last element -1)

    while True:
        for i in range(r - 1, -1, -1):  # Loop in range from repeats to 0
            # If element i from indices is smaller then length of iterable_elements list
            if indices[i] < iterable_elements_len:
                # Set the value of indices located after i element as value "indices[i] + 1"
                incremented_indices_value = indices[i] + 1
                indices[i:] = [incremented_indices_value for _ in range(0, r - i)]
                yield tuple(iterable_elements[i] for i in indices)  # Yield these values
                # The next iteration continues from here
                break  # Restarting loop
        else:
            # If the for loop ended successfully (no 'break')
            # - that means all the combinations with replacement were yield already
            return None  # Stopping the program


def main():
    pass


if __name__ == '__main__':
    main()
    
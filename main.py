"""Itertools module"""
from typing import Iterable


def count(start=0, step=1):
    """
    Returns iterable object of endless cycle.
    Usage:
    count() -> 0, 1, 2, ...
    count(8, 6) -> 8, 14, 20, ...
    count(0, 0) -> 0
    """
    if step == 0:
        yield start
    else:
        while True:
            yield start
            start += step


def cycle(iterable):
    """
    Returns iterator with values
    which are in iterable object.
    cycle(['A', 'B', 'C']) -> A, B, C, A, B, C, ...
    cycle(['ABCA']) -> A, B, C, A, A, B, ...
    cycle(('C')) -> C, C, C, ...
    """
    lenght = len(iterable)
    if lenght == 0:
        return iterable
    else:
        while True:
            for item in iterable:
                yield item


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
    [('A', '1'), ('A', '2'), ('A', '3'), ('B', '1'), ('B', '2'), \
('B', '3'), ('C', '1'), ('C', '2'), ('C', '3')]
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
            elements = self.args * self.repeat
            result = [[]]
            # Iterate through elements in order to create combinations
            for element in elements:
                result = [array + [item] for array in result for item in element]
            # Wrap elements into tuples and yield them
            for element in result:
                yield tuple(element)
    def __str__(self):
        return f"Product(args: {self.args}, repeat={self.repeat})"


def permutations(iterable, r=None):
    """
    Return successive r length permutations of elements in the iterable.
    If r is not specified or is None, then r defaults to the
    length of the iterable and all possible full-length permutations are generated.
    >>> list(permutations("ABCD", 2))[:3]
    [('A', 'B'), ('A', 'C'), ('A', 'D')]
    """
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)


def combinations(iterable, r):
    """
    Returns sorted compinations of length r in iterable.
    Permutations is used to get all possible combinations, then the sorted ones are picked out.
    >>> list(combinations("ABCD", 2))
    [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
    """
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)

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
    >>> list(combinations_with_replacement(['1', '2', '3', '4'], 3))
    [('1', '1', '1'), ('1', '1', '2'), ('1', '1', '3'), ('1', '1', '4'), \
('1', '2', '2'), ('1', '2', '3'), ('1', '2', '4'), ('1', '3', '3'), \
('1', '3', '4'), ('1', '4', '4'), ('2', '2', '2'), ('2', '2', '3'), \
('2', '2', '4'), ('2', '3', '3'), ('2', '3', '4'), ('2', '4', '4'), \
('3', '3', '3'), ('3', '3', '4'), ('3', '4', '4'), ('4', '4', '4')]
    >>> len(list(combinations_with_replacement([element for element in range(100)], 3)))
    171700
    >>> list(combinations_with_replacement('ABC', -999))
    Traceback (most recent call last):
        ...
    ValueError: r must be non-negative
    >>> list(combinations_with_replacement(111, 2))
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not iterable
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()


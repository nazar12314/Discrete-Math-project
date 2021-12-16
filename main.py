"""Itertools module"""


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


def combinations_with_replacement(r, n):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
    
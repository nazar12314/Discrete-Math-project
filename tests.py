"""
Tests for iter_tools module
"""
import main

def count_test(start: int, step: int, last: int) -> list:
    """
    Returns a sequence from a start number
    to limit with certain step.
    >>> len(count_test(1, 1, 10**8))
    100000000
    >>> count_test(0, 10, 100)
    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    >>> len(count_test(1, 1, 10**2))
    100
    >>> count_test(0, 1, 10)[1]
    [1]
    >>> count_test(0, 0, 0)
    [0]
    """
    number_list = []
    for element in main.count(start, step):
        if element <= last:
            number_list.append(element)
        else:
            break
    return number_list


def cycle_test(iterable, last: int) -> list:
    """
    Returns a sequence with limited length.
    >>> cycle_test('DIMA', 8)
    ['D', 'I', 'M', 'A', 'D', 'I', 'M', 'A']
    >>> cycle_test(['C', 'A', 'T'], 9)
    ['C', 'A', 'T', 'C', 'A', 'T', 'C', 'A', 'T']
    >>> cycle_test('TEODOR', 8)
    ['T', 'E', 'E', 'D', 'O', 'R', 'T', 'E']
    >>> cycle_test('', 1)
    []
    """
    fin_list = []

    for element in main.cycle(iterable):
        if len(fin_list) < last:
            fin_list.append(element)
        else:
            break
    return fin_list

assert len(count_test(1, 1, 10**8)) == 10**8
assert count_test(0, 10, 100) == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
assert len(count_test(1, 1, 10**2)) == 100
assert list(count_test(0, 1, 10))[1] == 1
assert count_test(0, 0, 0) == [0]
assert cycle_test('DIMA', 8) == ['D', 'I', 'M', 'A', 'D', 'I', 'M', 'A']
assert cycle_test(['C', 'A', 'T'], 9) == ['C', 'A', 'T', 'C', 'A', 'T', 'C', 'A', 'T']
assert cycle_test('TEODOR', 8) == ['T', 'E', 'O', 'D', 'O', 'R', 'T', 'E']
assert cycle_test('', 1) == []
assert len(list(main.repeat('ABC', 1000))) == 1000
assert list(main.repeat('ABC', 3)) == ['ABC', 'ABC', 'ABC']
assert list(main.repeat('aBcDeHiJ', 5)) == ['aBcDeHiJ', 'aBcDeHiJ', 'aBcDeHiJ', 'aBcDeHiJ', 'aBcDeHiJ']
assert list(main.repeat('test', 0)) == []
assert list(main.repeat('', 1)) == ['']
assert len(list(main.product([1, 2, 3], repeat=2))) == 9
assert list(main.product('AB', repeat=2)) == [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
assert list(main.product(['A', 'B'], repeat=2)) == [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
assert list(main.product([], repeat=2)) == []
assert list(main.permutations('abc', 2)) == [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
assert list(main.permutations(['a', 'b', 'c'], 2)) == [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
assert list(main.permutations([['a'], ['b']], 3)) == []
assert list(main.permutations('abc', 1)) == [('a',), ('b',), ('c',)]
assert list(main.combinations_with_replacement('ABC', 2)) == [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
assert list(main.combinations_with_replacement(['1', '2', '3', '4'], 3)) == [
    ('1', '1', '1'), ('1', '1', '2'), ('1', '1', '3'), ('1', '1', '4'),
    ('1', '2', '2'), ('1', '2', '3'), ('1', '2', '4'), ('1', '3', '3'),
    ('1', '3', '4'), ('1', '4', '4'), ('2', '2', '2'), ('2', '2', '3'),
    ('2', '2', '4'), ('2', '3', '3'), ('2', '3', '4'), ('2', '4', '4'),
    ('3', '3', '3'), ('3', '3', '4'), ('3', '4', '4'), ('4', '4', '4')
]
assert len(list(main.combinations_with_replacement(list(range(100)), 3))) == 171700
assert list(main.combinations_with_replacement('ABC', 0)) == [()]
assert list(main.combinations_with_replacement('', 10)) == []
assert list(main.combinations(range(4), 3)) == [(0,1,2), (0,1,3), (0,2,3), (1,2,3)]
assert len(set(main.combinations(range(100), 3))) == 161700


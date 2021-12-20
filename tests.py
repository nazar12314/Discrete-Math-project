"""
Tests for iter_tools module
"""
import main

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


"""
Tests for iter_tools module
"""
import main

assert len(list(main.repeat('ABC', 1000))) == 1000
assert list(main.repeat('ABC', 3)) == ['ABC', 'ABC', 'ABC']
assert list(main.repeat('aBcDeHiJ', 5)) == ['aBcDeHiJ', 'aBcDeHiJ', 'aBcDeHiJ', 'aBcDeHiJ', 'aBcDeHiJ']
assert list(main.repeat('test', 0)) == []
assert list(main.repeat('', 1)) == ['']
assert len(list(main.product([1, 2, 3], repeat = 2))) == 9
assert list(main.product('AB', repeat = 2)) == [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
assert list(main.product(['A', 'B'], repeat = 2)) == [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
assert list(main.product([], repeat = 2)) == []
assert list(main.permutations('abc', 2)) == [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
assert list(main.permutations(['a', 'b', 'c'], 2)) == [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
assert list(main.permutations([['a'], ['b']], 3)) == []
assert list(main.permutations('abc', 1)) == [('a',), ('b',), ('c',)]


if __name__ == "__main__":
    import doctest
    print(doctest.testfile("main.py"))


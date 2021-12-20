# Itertools (19th team)
[![Tests](https://github.com/nazar12314/Discrete-Math-project/actions/workflows/test.yml/badge.svg)](https://github.com/nazar12314/Discrete-Math-project/actions/workflows/test.yml)
## Description
Our version of the Python itertools module.
### Functions
- count (Dmytro)
- cycle (Dmytro)
- repeat (Nazar)
- product (Nazar)
- permutations (Teodor)
  Generates successive r length permutations of an iterable.
  If r is not specified it defaults to the length of the iterable.
  Iterates over the Cartesian square of the range function using the product function.
  Yields a tuple by using the indices from the Cartesian square
- combinations (Nadia)
- combinations_with_replacement (Serhii)
  Generates successive r length combinations of elements in the iterable allowing individual elements to have successive repeats.
  The combination tuples are emitted in lexicographic ordering according to the order of the input iterable.
  Elements are treated as unique based on their position, not on their value.
## Contributors (19-th team)
- Teodor Muzychuk (permutations, tests.py, README.md, GitHub actions)
- Nazar Kononenko (repeat, product, GitHub management)
- Serhii Matsyshyn (combinations_with_replacement)
- Nadia Lakoma (combinations)
- Dmytro Yevchenko (count, cycle)

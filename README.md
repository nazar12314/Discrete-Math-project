# Itertools (12th team)
[![Tests](https://github.com/nazar12314/Discrete-Math-project/actions/workflows/test.yml/badge.svg)](https://github.com/nazar12314/Discrete-Math-project/actions/workflows/test.yml)
## Description
Our version of the Python itertools module.
The average time complexity of all functions is O(n).
With large workloads, the execution time shouldn't exceed 5 minutes, with smaller ones - 3-5 seconds.
The algorithms were made according to the Python Documentation.
The tests.py module contains the tests for all the functions, and is run via github actions.
### Functions
- count (Dimitriy)
Returns iterable object of endless cycle.
- cycle (Dimitriy)
Returns iterator with values which are in iterable object.
- repeat (Nazar)
- ```python
  repeat(value, amount=None) -> Generator
  ```
  Repeat(object [,times]) -> create an iterator which returns the object for the specified number of times.
  If 'amount' is not specified, returns the object endlessly
- product (Nazar)
- ```python
    product(*iterables, repeat=1) -> Generator
   ```
  Returns cartesian product of input iterables
  Receives as a parameter an array of data, consisting of several groups of values.
 # Example of usage:
 - ```python
    product('abc', '123', ['2', '3'], [1, 2, 3], repeat=2)
    product(range(100), range(1000))
   ```
  This product function allows you to get a new set of groups in all possible variations
  from an entered sequence of numbers or characters.
  To compute the product of an iterable with itself,
  specify the number of repetitions with the optional 'repeat' keyword argument.
  For example, product(A, repeat=4) means the same as product(A, A, A, A).
- permutations (Teodor)
  Generates successive r length permutations of an iterable.
  If r is not specified it defaults to the length of the iterable.
  Iterates over the Cartesian square of the range function using the product function.
  Yields a tuple by using the indices from the Cartesian square
- combinations (Nadia)
  Returns sorted combinations of length r in iterable.
  Permutations is used to get all possible combinations, then the sorted ones are picked out.
- combinations_with_replacement (Serhii)
  Generates successive r length combinations of elements in the iterable allowing individual elements to have successive repeats.
  The combination tuples are emitted in lexicographic ordering according to the order of the input iterable.
  Elements are treated as unique based on their position, not on their value.
## Usage 
    import main
    main.function(args)
## Contributors (12-th team)
- Teodor Muzychuk (permutations, tests.py, README.md, GitHub actions)
- Nazar Kononenko (repeat, product, GitHub management)
- Serhii Matsyshyn (combinations_with_replacement)
- Nadia Lakoma (combinations)
- Dimitriy Yevchenko (count, cycle)
## License
Apache license. See LICENSE.

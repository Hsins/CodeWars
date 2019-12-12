# Enumerable Magic #25 - Take the First N Elements

## Information

- KYU: 8
- Link: [Enumerable Magic #25 - Take the First N Elements](https://www.codewars.com/kata/enumerable-magic-number-25-take-the-first-n-elements/train/python)

## Description:

Create a method take that accepts a list/array and a number n, and returns a list/array array of the first n elements from the list/array.

If you need help, here's a reference:

- [Python Document | Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

## My Solution

```python
def take(arr, n):
    return arr[:n]
```

## Lambda Solutions

```python
take=lambda arr, n: arr[:n]
```
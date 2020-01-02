# Find All Occurrences of An Element in An Array

## Information

- KYU: 7
- Link: [Find All Occurrences of An Element in An Array](https://www.codewars.com/kata/find-all-occurrences-of-an-element-in-an-array/train/python)

## Description:

Given an array (a list in Python) of integers and an integer `n`, find all occurrences of `n` in the given array and return another array containing all the index positions of `n` in the given array.

If `n` is not in the given array, return an empty array `[]`.

Assume that `n` and all values in the given array will always be integers.

**Example**:

```
find_all([6, 9, 3, 4, 3, 82, 11], 3)
> [2, 4]
```

## My Solution

```python
def find_all(array, n):
    return [idx for idx, num in enumerate(array) if num == n]
```

# Merging Sorted Integer Arrays (Without Duplicates)

## Information

- KYU: 8
- Link: [Merging Sorted Integer Arrays (Without Duplicates)](https://www.codewars.com/kata/merging-sorted-integer-arrays-without-duplicates/train/python)

## Description:

Write a function that merges two sorted arrays into a single one. The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate.

## My Solution

```python
def merge_arrays(first, second): 
    return sorted(set(first + second))
```

## Clever Solutions

```python
def merge_arrays(first, second):
    return sorted(set(first) | set(second))
```
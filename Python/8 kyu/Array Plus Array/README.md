# Array Plus Array

## Information

- KYU: 8
- Link: [Array Plus Array](https://www.codewars.com/kata/array-plus-array/train/python)

## Description:

I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.

## My Solution

```python
def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)
```

## Clever Solutions

```python
def array_plus_array(arr1, arr2):
    return sum(arr1 + arr2)
```
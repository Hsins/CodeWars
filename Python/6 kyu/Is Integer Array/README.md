# Is Integer Array

## Information

- KYU: 6
- Link: [Is Integer Array](https://www.codewars.com/kata/is-integer-array/train/python)

## Description:

Write a function with the signature shown below:

```
def is_int_array(arr):
    return True
```

- returns `true / True` if every element in an array is an integer or a float with no decimals.
- returns `true / True` if array is empty.
- returns `false / False` for every other input.

## My Solution

```python
def is_int_array(arr):
    return isinstance(arr, list) and all(isinstance(x, (int, float)) and x == int(x) for x in arr)
```

# What is Between?

## Information

- KYU: 8
- Link: [What is Between?](https://www.codewars.com/kata/what-is-between/train/python)

## Description:

Write a function taking two parameters and returning an int array of all elements between the input parameters and including them.

## My Solution

```python
def between(a, b):
    return list(range(a, b + 1))
```

## Lambda Solutions

```python
between = lambda a, b: list(range(a, b + 1))
```
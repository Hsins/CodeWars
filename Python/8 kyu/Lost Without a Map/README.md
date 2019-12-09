# Lost Without a Map

## Information

- KYU: 8
- Link: [Lost Without a Map](https://www.codewars.com/kata/beginner-lost-without-a-map/train/python)

## Description:

Given an array of integers, return a new array with each value doubled.

For example:

```
[1, 2, 3] --> [2, 4, 6]
```

For the beginner, try to use the `map` method - it comes in very handy quite a lot so is a good one to know.

## My Solution

```python
def maps(a):
    return list(map(lambda x: 2 * x, a))
```

## Clever Solutions

```python
def maps(a):
    return [2 * x for x in a]
```
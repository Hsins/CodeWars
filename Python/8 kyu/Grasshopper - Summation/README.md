# Grasshopper - Summation

## Information

- KYU: 8
- Link: [Grasshopper - Summation](https://www.codewars.com/kata/grasshopper-summation/train/python)

## Description:

Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

**Example**:

```
summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
```

## My Solution

```python
def summation(num):
    return sum(range(1, num + 1))
```

## Clever Solutions

```python
def summation(num):
    return (1 + num) * num / 2
```

## Lambda Solutions

```python
summation = lambda num: sum(range(1, num + 1))
```
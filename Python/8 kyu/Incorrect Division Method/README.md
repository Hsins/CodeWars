# Incorrect Division Method

## Information

- KYU: 8
- Link: [Incorrect Division Method](https://www.codewars.com/kata/incorrect-division-method/train/python)

## Description:

This method, which is supposed to return the result of dividing its first argument by its second, isn't always returning correct values. Fix it.

```python
def divide_numbers(x, y):
    return x / y
```

## My Solution

```python
from __future__ import division


def divide_numbers(x, y):
    return x / y
```

有點累贅的題目，由於 Python 2 已經不再維護，並不是很需要在意這題。

## Clever Solutions

```python
def divide_numbers(x,y):
    return float(x) / y
```
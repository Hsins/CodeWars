# Regexp Basics - Is It a Digit?

## Information

- KYU: 8
- Link: [Regexp Basics - Is It a Digit?](https://www.codewars.com/kata/regexp-basics-is-it-a-digit/train/python)

## Description:

Implement `String#digit?` (in Java `StringUtils.isDigit(String)`), which should return `true` if given object is a digit (0-9), `false` otherwise.

## My Solution

```python
import re


def is_digit(n):
    return bool(re.fullmatch(r'^[0-9]$', n))
```

## Clever Solutions

```python
import re

def is_digit(n):
    return bool(re.match("\d\Z", n))
```
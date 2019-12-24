# Simple Validation of a Username with Regex

## Information

- KYU: 8
- Link: [Simple Validation of a Username with Regex](https://www.codewars.com/kata/simple-validation-of-a-username-with-regex/train/python)

## Description:

Write a simple regex to validate a username. Allowed characters are:

- lowercase letters,
- numbers,
- underscore

Length should be between 4 and 16 characters (both included).

## My Solution

```python
import re


def validate_usr(username):
    pattern = re.compile("^[a-z0-9_]{4,16}$")
    return bool(pattern.match(username))
```

```python
import re


def validate_usr(username):
    return bool(re.match("^[a-z0-9_]{4,16}$", username))
```

## Clever Solutoins

```python
import re


def validate_usr(un):
    return re.match('^[a-z0-9_]{4,16}$', un) != None
```

## Lambda Solutions

```python
import re


validate_usr = lambda username: bool(re.match('^[a-z\d_]{4,16}$', username))
```

## References

- [Python Document | `re` — Regular expression operations](https://docs.python.org/3/library/re.html)

# Remove First and Last Character

## Information

- KYU: 8
- Link: [Remove First and Last Character](https://www.codewars.com/kata/remove-first-and-last-character/train/python)

## Description:

It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

## My Solution

```python
def remove_char(s):
    return s[1:-1]
```

## Lambda Solutions

```python
remove_char = lambda s: s[1:-1]
```
# 5 Without Numbers!!

## Information

- KYU: 8
- Link: [5 Without Numbers!!](https://www.codewars.com/kata/5-without-numbers/train/python)

## Description:

Write a function that always returns `5`

Sounds easy right? Just bear in mind that you can't use any of the following characters: `0123456789*+-/`

Good luck :)

## My Solution

```python
def unusual_five():
    return len("     ")
```

## Lambda Solutions

```python
unusual_five = lambda: ord("")
```
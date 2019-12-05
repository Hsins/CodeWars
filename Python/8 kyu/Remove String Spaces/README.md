# Remove String Spaces

## Information

- KYU: 8
- Link: [Remove String Spaces](https://www.codewars.com/kata/remove-string-spaces/train/python)

## Description:

Simple, remove the spaces from the string, then return the resultant string.

## My Solution

```python
def no_space(x):
    return x.replace(" ", "")
```

## Clever Solutions

```python
def no_space(x):
    return "".join(x.split())
```

## Lambda Solutions

```python
no_space = lambda s: ''.join(filter(lambda ch: not ch == ' ', s))
```

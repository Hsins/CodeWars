# Even or Odd

## Information

- KYU: 8
- Link: [Even or Odd](https://www.codewars.com/kata/even-or-odd/train/python)

## Description:

Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

## My Solution

```python
def even_or_odd(number):
    return "Odd" if number % 2 else "Even"
```

## Clever Solutions

```python
def even_or_odd(number):
  return ["Even", "Odd"][number % 2]
```

## Lambda Solutions

```python
even_or_odd = lambda number: "Odd" if number % 2 else "Even"
```
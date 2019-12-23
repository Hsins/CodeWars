# Summing a Number's Digits

## Information

- KYU: 7
- Link: [Summing a Number's Digits](https://www.codewars.com/kata/summing-a-numbers-digits/train/python)

## Description:

Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits. For example:

```
sum_digits(10)  # Returns 1
sum_digits(99)  # Returns 18
sum_digits(-32) # Returns 5
```

Let's assume that all numbers in the input will be integer values.

## My Solution

```python
def sum_digits(number):
    return sum(map(int, str(abs(number))))
```

## Clever Solutions

```python
def sumDigits(number):
    return sum(int(d) for d in str(abs(number)))
```


# Square Every Digit

## Information

- KYU: 7
- Link: [Square Every Digit](https://www.codewars.com/kata/square-every-digit/train/python)

## Description:

Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run `9119` through the function, `811181` will come out, because `9^2` is `81` and `1^2` is `1`.

**Note**: The function accepts an integer and returns an integer

## My Solution

```python
def square_digits(num):
    return int(''.join(str(int(_)**2) for _ in str(num)))
```

## Clever Solutions

```python
def square_digits(num):
    retult = ""
    for digit in str(num):
        retult += str(int(digit)**2)
    return int(retult)
```

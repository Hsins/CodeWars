# Sum The Strings

## Information

- KYU: 8
- Link: [Sum The Strings](https://www.codewars.com/kata/sum-the-strings/train/python)

## Description:

Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

```
sumStr("4", "5")    // should output "9"
sumStr("34", "5")   // should output "39"
```

If either input is an empty string, consider it as zero.

## My Solution

```python
def sum_str(a, b):
    a = int(a) if a else 0
    b = int(b) if b else 0
    return str(a + b)
```

## Clever Solutions

```python
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))
```

```python
def sum_str(*args):
    return str(sum(map(lambda x: int(x) if x else 0, args)))
```

## Lambda Solutions

```python
sum_str = lambda *args: str(sum(int(x) for x in args if x))
```

# Sum Mixed Array

## Information

- KYU: 8
- Link: [Sum Mixed Array](https://www.codewars.com/kata/sum-mixed-array/train/python)

## Description:

Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.

## My Solution

```python
def sum_mix(arr):
    return sum([int(num) for num in arr])
```

## Clever Solutions

```python
def sum_mix(arr):
    return sum(map(int, arr))
```

## Lambda Solutions

```python
sum_mix = lambda arr: sum(map(int, arr))
```

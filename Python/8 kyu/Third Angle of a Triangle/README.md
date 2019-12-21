# Third Angle of a Triangle

## Information

- KYU: 8
- Link: [Third Angle of a Triangle](https://www.codewars.com/kata/third-angle-of-a-triangle/train/python)

## Description:

You are given two angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.

## My Solution

```python
def other_angle(a, b):
    return 180 - a - b
```

## Lambda Solutions

```python
other_angle = lambda a, b: 180 - (a + b)
```
# Surface Area and Volume of a Box

## Information

- KYU: 8
- Link: [Surface Area and Volume of a Box](https://www.codewars.com/kata/surface-area-and-volume-of-a-box/train/python)

## Description:

Write a function that returns the total surface area and volume of a box as an array: `[area, volume]`

## My Solution

```python
def get_size(w,h,d):
    return [2 * (w*h + h*d + d*w), w * h * d]
```

## Lambda Solutions

```python
get_size = lambda w, h, d: [2 * (w*h + w*d + h*d), w * h * d]
```
# Keep Hydrated

## Information

- KYU: 8
- Link: [Keep Hydrated](https://www.codewars.com/kata/keep-hydrated-1/train/python)

## Description:

Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

**Example**:

```
time = 3 ----> litres = 1
time = 6.7---> litres = 3
time = 11.8--> litres = 5
```

## My Solution

```python
import math


def litres(time):
    return math.floor(time * 0.5)
```

## Clever Solutions

```python
def litres(time):
    return time // 2
```

## Lambda Solutions

```python
litres = lambda time: time // 2
```
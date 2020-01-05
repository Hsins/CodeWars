# Tip Calculator

## Information

- KYU: 8
- Link: [Tip Calculator](https://www.codewars.com/kata/tip-calculator/train/python)

## Description:

Complete the function, which calculates how much you need to tip based on the total amount of the bill and the service.

You need to consider the following ratings:

- Terrible: tip 0%
- Poor: tip 5%
- Good: tip 10%
- Great: tip 15%
- Excellent: tip 20%

The rating is **case insensitive** (so "great" = "GREAT"). If an unrecognised rating is received, then you need to return:

- `"Rating not recognised"` in Javascript, Python and Ruby...
- ...or `null` in Java
- ...or `-1` in C#

Because you're a nice person, you always round up the tip, regardless of the service.

## My Solution

```python
from math import ceil


def calculate_tip(amount, rating):
    rating_dict = {'TERRIBLE': 0, 'POOR': 0.05,
                   'GOOD': 0.10, 'GREAT': 0.15, 'EXCELLENT': 0.20}

    try:
        return ceil(amount * rating_dict[rating.upper()])
    except KeyError:
        return "Rating not recognised"

```

## Clever Solutions

```python
from math import ceil


def calculate_tip(amount, rating):
    tipTypes = ["terrible", "poor", "good", "great", "excellent"]

    if rating.lower() in tipTypes:
        return ceil(amount * tipTypes.index(rating.lower()) * 0.05)
    else:
        return "Rating not recognised"
```
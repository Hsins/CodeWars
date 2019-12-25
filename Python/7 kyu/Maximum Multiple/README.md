# Maximum Multiple

## Information

- KYU: 7
- Link: [Maximum Multiple](https://www.codewars.com/kata/maximum-multiple/train/python)

## Description:

**Given a Divisor and a Bound**, find the largest integer `N`. Such that:

- `N` is divisible by divisor
- `N` is less than or equal to bound
- `N` is greater than 0.

**Note**

- The parameters (divisor, bound) passed to the function are only positve values .
- It's guaranteed that a divisor is Found .

**Example**

```
maxMultiple (2,7) ==> return (6)
Explanation:
(6) is divisible by (2) , (6) is less than or equal to bound (7) , and (6) is > 0 .

maxMultiple (10,50)  ==> return (50)
Explanation:
(50) is divisible by (10) , (50) is less than or equal to bound (50) , and (50) is > 0 .*

maxMultiple (37,200) ==> return (185)
Explanation:
(185) is divisible by (37) , (185) is less than or equal to bound (200) , and (185) is > 0 .
```

## My Solution

```python
def max_multiple(divisor, bound):
    return bound // divisor * divisor
```

## Clever Solutions

```python
def max_multiple(divisor, bound):
    return bound - (bound % divisor)
```

## Lambda Solutions

```python
max_multiple = lambda divisor, bound: bound - (bound % divisor)
```

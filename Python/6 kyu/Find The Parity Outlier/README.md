# Find The Parity Outlier

## Information

- KYU: 6
- Link: [Find The Parity Outlier](https://www.codewars.com/kata/find-the-parity-outlier/train/python)

## Description:

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer `N`. Write a method that takes the array as an argument and returns this "outlier" `N`.

**Examples**:

```
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
```

## My Solution

```python
def find_outlier(integers):
    is_odd = True if (integers[0] % 2 + integers[1] % 2 + integers[2] % 2) < 2 else False

    if is_odd:
        for integer in integers:
            if integer % 2:
                return integer
    else:
        for integer in integers:
            if not integer % 2:
                return integer
```

## Clever Solutions

```python
def find_outlier(integers):
    odds  = [x for x in integers if x % 2 != 0]
    evens = [x for x in integers if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]
```

一個滿巧妙但是效率並不是非常好的解法，將原來的列表分別遍歷兩次取出奇數值和偶數值，回傳長度較少的列表的首位值（只有一個）。

```python
def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]
```

上面解法的一個變形，只需要進行一次遍歷找出每一個數除二的餘數陣列。當餘數總和等於一時找奇數，不唯一時找偶數。

```python
def find_outlier(integers):
    bit = ((integers[0] & 1) + (integers[1] & 1) + (integers[2] & 1)) >> 1

    for n in integers:
        if (n & 1) ^ bit:
            return n
```

- 位元運算符 `&` 會對二進制數進行 `AND` 操作，藉此來判斷奇偶數。
- 位元運算符 `>>` 和 `<<` 會對二進制數進行移位操作，其中 `<<` 是左移，相當於將原來數字乘二，`>>` 是右移，相當於將原來數字除二，藉此來判斷要在陣列中尋找的是奇數還是偶數。

```python
def find_outlier(integers):
    bit = integers[0] & 1

    if integers[1] & 1 != bit:
        return integers[integers[2] & 1 == bit]

    for n in integers:
        if n & 1 != bit:
            return n
```

## References

- [Python Wiki | FAQ: What do the operators <<, >>, &, |, ~, and ^ do?](https://wiki.python.org/moin/BitwiseOperators)
- [stackoverflow | What does & mean in python](https://stackoverflow.com/questions/8556206/what-does-mean-in-python)
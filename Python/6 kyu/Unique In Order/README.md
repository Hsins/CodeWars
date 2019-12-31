# Unique In Order

## Information

- KYU: 6
- Link: [Unique In Order](https://www.codewars.com/kata/unique-in-order/train/python)

## Description:

Implement the function `unique_in_order` which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

**Example**:

```
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
```

## My Solution

```python
def unique_in_order(iterable):
    result = []
    for item in iterable:
        if len(result) == 0 or item != result[-1]:
            result.append(item)

    return result
```

## Clever Solutions

```python
from itertools import groupby

def unique_in_order(iterable):
    return [key for (key, group) in groupby(iterable)]
```

這個解法用到了 Python 標準函數庫 `itertools` 中的 [`groupby()`](https://docs.python.org/3/library/itertools.html#itertools.groupby) 函數。這也剛好用到他的特性之一，很多人在使用時遇到的坑就是沒有考慮到該函數的斷點，所以沒有先將迭代物件進行排序就使用 `groupby()`，而這題恰恰不需要排序（因為只需要連續的字元只計單個）。

```python
def unique_in_order(iterable):
    result = []
    prev = None
    for item in iterable:
        if item != prev:
            result.append(item)
            prev = item

    return result
```

這是很標準的 LeetCode 中關於鏈表（Linked List）的題目，在遍歷之前先額外設置一個值為 `None` 的頭節點是很常見的操作方式。

## Lambda Solutions

```python
unique_in_order = lambda iterable: [item for index, item in enumerate(iterable) if index == 0 or iterable[index - 1] != item]
```

## References

- [Python Documentation | itertools — Functions creating iterators for efficient looping](https://docs.python.org/3/library/itertools.html)
- [Real Python | Itertools in Python 3, By Example](https://realpython.com/python-itertools/)
# Reversed Strings

## Information

- KYU: 8
- Link: [Reversed Strings](https://www.codewars.com/kata/reversed-strings/train/python)

## Description:

Complete the solution so that it reverses the string value passed into it.

```
solution('world') # returns 'dlrow'
```

## My Solution

```python
def solution(string):
    return string[::-1]
```

## Clever Solutions

```python
def solution(string):
    return "".join(reversed(string))
```

利用了 Python 中字串的 `join()` 方法和 [迭代器協議（iterator protocol）](https://docs.python.org/3/c-api/iter.html#iterator-protocol)，其中內建函數 `reversed()` 會返回一個反轉的迭代器。
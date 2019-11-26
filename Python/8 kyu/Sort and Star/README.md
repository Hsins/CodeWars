# Sort and Star

## Information

- KYU: 8
- Link: [Sort and Star](https://www.codewars.com/kata/sort-and-star/train/python)

## Description:

You will be given an vector of string(s). You must sort it alphabetically (case-sensitive!!) and then return the first value.

The returned value must be a string, and have `"***"` between each of its letters.

You should not remove or add elements from/to the array.

## My Solution

```python
def two_sort(array):
    word = sorted(array)[0]
    return "***".join(word)
```

## Clever Solutions

```python
def two_sort(array):
    return '***'.join(min(array))
```

對於 Python3 來說，函數 `min()` 和 `max()` 作用在存放字串的陣列時，會使用字典序進行比較。也就是說：

- `min()` 會回傳陣列中，字串字典序最小者
- `max()` 會回傳陣列中，字串字典序最大者

關於這部份的內容，可以參考 [How does the max() function work on list of strings in python?](https://stackoverflow.com/questions/20463204/how-does-the-max-function-work-on-list-of-strings-in-python) 這篇回答。


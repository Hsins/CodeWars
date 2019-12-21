# Numbers to Letters

## Information

- KYU: 7
- Link: [Numbers to Letters](https://www.codewars.com/kata/numbers-to-letters/train/python)

## Description:

Given an array of numbers, you must return a string. The numbers correspond to the letters of the alphabet in reverse order: a=26, z=1 etc. You should also account for `'!'`, `'?'` and `' '` that are represented by '27', '28' and '29' respectively.

All inputs will be valid.

## My Solution

```python
def switcher(arr):
    letters = ' ?!abcdefghijklmnopqrstuvwxyz'
    return ''.join(letters[::-1][int(idx) - 1] for idx in arr)
```

## Clever Solutions

```python
import string


letters = string.ascii_lowercase[::-1] + '!? '
def switcher(arr):
    return ''.join([letters[idx - 1] for idx in map(int, arr) if idx])
```

套件 [`string`](https://docs.python.org/3/library/string.html) 中，可以直接使用參數 `string.ascii_lowercase` 取得所有小寫的英文字母（照順序排列）。

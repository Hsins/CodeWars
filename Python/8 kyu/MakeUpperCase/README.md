# MakeUpperCase

## Information

- KYU: 8
- Link: [MakeUpperCase](https://www.codewars.com/kata/makeuppercase/train/python)

## Description:

Write function makeUpperCase.

## My Solution

```python
def make_upper_case(s):
    return s.upper()
```

## Clever Solutions

```python
def make_upper_case(s):
    return ''.join(chr(ord(c)-32) for c in s)
```

參考 [Python Reference | ASCII Chart](https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html) 中的內容，可以知道大小寫字母之間在使用 `ord()` 方法之後轉換成數字時差了 32，所以可以逐個字元轉成大寫字元。
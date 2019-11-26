# Double Char

## Information

- KYU: 8
- Link: [Double Char](https://www.codewars.com/kata/double-char/train/python)

## Description:

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

```
double_char("String") ==> "SSttrriinngg"
double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"
double_char("1234!_ ") ==> "11223344!!__  "
```

Good Luck!

## My Solution

```python
def double_char(s):
    result = ""
    for c in s:
        result += c * 2

    return result
```

## Clever Solutions

```python
def double_char(s):
    return ''.join(c * 2 for c in s)
```

透過 Python 的[生成器表達式（generator expression）](https://www.python.org/dev/peps/pep-0289/)迭代處理字串中的每一個字符，並透過字串的 `join()` 方法串接。此處值得注意的是生成器表達式和列表推導雖然看起來很相像，但本質上是不同的東西，關於相關的比較可以閱讀 [List Comprehension vs Generator Expressions in Python](https://code-maven.com/list-comprehension-vs-generator-expression) 一文。

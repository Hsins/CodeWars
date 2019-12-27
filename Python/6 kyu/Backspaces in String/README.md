# Backspaces in String

## Information

- KYU: 6
- Link: [Backspaces in String](https://www.codewars.com/kata/backspaces-in-string/train/python)

## Description:

Assume `"#"` is like a backspace in string. This means that string `"a#bc#d"` actually is `"bd"`

Your task is to process a string with `"#"` symbols.

**Examples**

```
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
```

## My Solution

```python
def clean_string(string):
    result = ""

    for char in string:
        if char == "#":
            result = result[:-1]
        else:
            result += char

    return result
```

## Clever Solutions

```python
def clean_string(string):
    stack = []

    for char in string:
        if char=='#' and stack:
            stack.pop()
        elif char!='#':
            stack.append(char)

    return ''.join(stack)
```

常見的堆疊（stack）應用題，逐個遍歷字串中的字元，當遇到字元為 `#` 時，將堆疊中的尾巴元素彈出。

```python
import re

def clean_string(string):
    while '#' in string:
        string = re.sub('.?#', '', string, count=1)
    return string
```

使用正則表達式，只要字串中還有 `#` 字元，就進行替換。

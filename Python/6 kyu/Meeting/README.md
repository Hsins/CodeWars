# Meeting

## Information

- KYU: 6
- Link: [Meeting](https://www.codewars.com/kata/meeting/train/python)

## Description:

John has invited some friends. His list is:

```
s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
```

Could you make a program that

- makes this string uppercase
- gives it sorted in alphabetical order by last name.

When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.

So the result of function `meeting(s)` will be:

```
"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
```

It can happen that in two distinct families with the same family name two people have the same first name too.

**Notes**

- You can see another examples in the `"Sample Tests"`.

## My Solution

```python
def meeting(s):
    names = []
    friends = ""

    for _ in s.upper().split(";"):
        names.append(_.split(":")[::-1])

    for name in sorted(names):
        friends += '({}, {})'.format(name[0], name[1])

    return friends
```

## Clever Solutions

```python
def meeting(s):
    names = s.upper().split(';')
    return ''.join(sorted('({1}, {0})'.format(*(n.split(':'))) for n in names))
```

這段代碼一開始看到時可能不太容易理解，但其實邏輯都是一樣的：

1. 首先透過字串的 `upper()` 方法和 `split()` 方法將原有字串中的所有字符都轉為大寫，並以 `';'` 字元為分隔拆分至陣列 `names` 中，此時陣列 `names` 中所儲存的是一個個 `LAST_NAME:FIRST_NAME` 結構的字串。
2. 透過生成器表達式將逐個處理陣列中的每一個字串 `n`，其中 `n.split(':')` 為一個陣列，其中儲存的內容為 `['LAST_NAME', 'FIRST_NAME']` 的結構。
3. 使用星號表達式（Starred Expression）取出陣列內容，並放入 `({1}, {0})` 的結構中。
4. 最後透過 `join()` 方法串接。

## Lambda Solutions

```python
meeting = lambda s: ''.join(sorted('({1}, {0})'.format(*w.split(':')).upper() for w in s.split(';')))
```
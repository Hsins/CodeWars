# Your Order, Please

## Information

- KYU: 6
- Link: [Your Order, Please](https://www.codewars.com/kata/your-order-please/train/python)

## Description:

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

**Note**: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

**Examples**:

```
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
```

## My Solution

```python
def order(sentence):
    result = ''
    words = sentence.split()

    for _ in range(1, 10):
        for word in words:
            if word.count(str(_)) == 1:
                result += f'{word} '

    return result[:-1]
```

## Clever Solutions

```python
def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda word: int(list(filter(str.isdigit, word))[0])))
```

Python 所提供的內建函數 `sorted()` 可以傳入 `key` 參數作為排序的依據，此處透過 `filter()` 找出每一個字中的數字再進行排序。順帶一題的是 Python3 中的 `filter()` 返回的值並非列表，而是一個迭代器物件。


```python
def order(words):
    return ' '.join(sorted(words.split(), key=lambda word: sorted(word)))
```

這個作法十分巧妙，因為在對一個含有數字的字串進行排序時，返回值會將數字字元放在第一位。

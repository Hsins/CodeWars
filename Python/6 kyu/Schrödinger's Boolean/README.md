# Schrödinger's Boolean

## Information

- KYU: 6
- Link: [Schrödinger's Boolean](https://www.codewars.com/kata/schrodingers-boolean/train/python)

## Description:

Can a value be both `True` and `False`?

Define `omnibool` so that it returns True for the following:

```
omnibool == True and omnibool == False
```

## My Solution

```python
class Omnibool:
    def __eq__(self, other):
        return True


omnibool = Omnibool()
```

在使用 `==` 運算符來比較兩個物件是否相等時，本質上是調用物件的 `__eq__()` 方法，最簡單的實作就是自定義物件的 `__eq__()` 方法，當不論和任何人比較時都回傳 `True`。

## Lambda Solutions

```python
omnibool = type('', (), {'__eq__': lambda * a: 1})()
```

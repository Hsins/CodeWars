# Area of a Square

## Information

- KYU: 8
- Link: [Area of a Square](https://www.codewars.com/kata/area-of-a-square/train/python)

## Description:

Complete the function that calculates the area of the red square, when the length of the circular arc A is given as the input. Return the result rounded to two decimals.

<p align="center">
  <img src="http://i.imgur.com/nJrae8n.png">
</p>

Note: use the `π` value provided in your language (`Math::PI`, `M_PI`, `math.pi`, etc)

## My Solution

```python
from math import pi


def square_area(A):
    return round((2 * A / pi) ** 2, 2)
```

## Lambda Solutions

```python
square_area = lambda A: round((2 * A / __import__('math').pi) ** 2, 2)
```

在使用 `import` 導入 Python 套件時，預設調用的是 `__import__()` 函數：

```
__import__(name, globals=None, locals=None, fromlist=(), level=0)
```

一般來說很少直接進行調用這個函數，通常是用在動態加載套件或延遲導入時，使用方法是：

```python
class LazyImport:
    def __init__(self, module_name):
        self.module_name = module_name
        self.module = None

    def __getattr__(self, name):
        if self.module is None:
            self.module = __import__(self.module_name)
        return getattr(self.module, name)

string = LazyImport("string")
print string.lowercase
```
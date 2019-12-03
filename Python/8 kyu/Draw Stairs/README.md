# Draw Stairs

## Information

- KYU: 8
- Link: [Draw Stairs](https://www.codewars.com/kata/draw-stairs/train/python)

## Description:

given a number `n`, draw stairs with `'I'` `n` tall and `n` wide, with the tallest in the top left. Example (with - to represent spaces; DO NOT USE THEM IN THE SOLUTIONS! USE SPACES IN SOLUTION! the "-"s are for clarity.): `draw_stairs(3) == '''I\n_I\n__I'''`

For example, a 7-step stairs should be drawn like this:

```
const sevenStepStairs = drawStairs(7);
```

```
I
 I
  I
   I
    I
     I
      I
```

## My Solution

```python
def draw_stairs(n):
    return '\n'.join(i * ' ' + 'I' for i in range(n))
```

## Clever Solutions

```python
def draw_stairs(n):
    return '\n'.join('I'.rjust(i + 1) for i in range(n))
```

Python 中字串的 [`rjust()`](https://docs.python.org/3/library/stdtypes.html?highlight=rjust#str.rjust) 方法會返回一個將原來字元靠右對齊，並使用空格（或指定字元）填充至長度 `width` 的字串。若指定的長度小於字串長度則會返回原字串。

## Lambda Solutions

```python
draw_stairs = lambda n: '\n'.join(i * ' ' + 'I' for i in range(n))
```

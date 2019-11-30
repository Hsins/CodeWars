# Calculating with Functions

## Information

- KYU: 5
- Link: [Calculating with Functions](https://www.codewars.com/kata/calculating-with-functions/train/python)

## Description:

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

```
seven(times(five()))    # must return 35
four(plus(nine()))      # must return 13
eight(minus(three()))   # must return 5
six(divided_by(two()))  # must return 3
```

**Requirements**:

- There must be a function for each number from 0 (`"zero"`) to 9 (`"nine"`)
- There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (`divided_by` in Ruby and Python)
- Each calculation consist of exactly one operation and two numbers
- The most outer function represents the left operand, the most inner function represents the right operand
- Divison should be integer division. For example, this should return `2`, not `2.666666`...: `eight(divided_by(three()))`

## My Solution

```python
def zero(func = None):
    return func(0) if func else 0
def one(func = None):
    return func(1) if func else 1
def two(func = None):
    return func(2) if func else 2
def three(func = None):
    return func(3) if func else 3
def four(func = None):
    return func(4) if func else 4
def five(func = None):
    return func(5) if func else 5
def six(func = None):
    return func(6) if func else 6
def seven(func = None):
    return func(7) if func else 7
def eight(func = None):
    return func(8) if func else 8
def nine(func = None):
    return func(9) if func else 9

def plus(y): 
    return lambda x: x + y
def minus(y):
    return lambda x: x - y
def times(y):
    return lambda x: x * y
def divided_by(y):
    return lambda x: x // y
```

## Clever Solutions

```python
def zero(arg=""):  return eval("0" + arg)
def one(arg=""):   return eval("1" + arg)
def two(arg=""):   return eval("2" + arg)
def three(arg=""): return eval("3" + arg)
def four(arg=""):  return eval("4" + arg)
def five(arg=""):  return eval("5" + arg)
def six(arg=""):   return eval("6" + arg)
def seven(arg=""): return eval("7" + arg)
def eight(arg=""): return eval("8" + arg)
def nine(arg=""):  return eval("9" + arg)

def plus(num):       return "+%s" % num
def minus(num):      return "-%s" % num
def times(num):      return "*%s" % num
def divided_by(num): return "/%s" % num
```

```python
id_ = lambda x: x
number = lambda x: lambda f=id_: f(x)
zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
plus = lambda x: lambda y: y + x
minus = lambda x: lambda y: y - x
times = lambda x: lambda y: y * x
divided_by = lambda x: lambda y: y / x
```
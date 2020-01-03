# Look and Say Numbers

## Information

- KYU: 6
- Link: [Look and Say Numbers](https://www.codewars.com/kata/look-and-say-numbers/train/python)

## Description:

There exists a sequence of numbers that follows the pattern

```
          1
         11
         21
        1211
       111221
       312211
      13112221
     1113213211
          .
          .
          .
```

Starting with "1" the following lines are produced by "saying what you see", so that line two is "one one", line three is "two one(s)", line four is "one two one one".

Write a function that given a starting value as a string, returns the appropriate sequence as a list. The starting value can have any number of digits. The termination condition is a defined by the maximum number of iterations, also supplied as an argument.

## My Solution

```python
from itertools import groupby


def look_and_say(data='1', maxlen=5):
    result = []
    for _ in range(0, maxlen):
        char_group = [list(group) for key, group in groupby(data)]
        result.append(''.join(f'{len(item)}{item[0]}' for item in char_group))
        data = result[-1]

    return result
```

## Clever Solutions

```python
from itertools import groupby


def look_and_say(data='1', maxlen=5):
    result = []
    for i in range(maxlen):
        data = "".join(str(len(list(group))) + str(key) for key, group in groupby(data))
        result.append(data)

    return result
```

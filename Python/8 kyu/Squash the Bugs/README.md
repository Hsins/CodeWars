# Squash the Bugs

## Information

- KYU: 8
- Link: [Squash the Bugs](https://www.codewars.com/kata/squash-the-bugs/train/python)

## Description:

Eliminate all bugs from the supplied code so that the code runs and outputs the expected value. Output should be the length of the longest word, as a number.

There will only be one 'longest' word.

```python
def find_longest(string):
    spl = str.split(" ")
    longest = 0
    i=0
    while (i > spl.length):
    if (spl(i).length > longest): longest = spl[i].length
    return longest
```

## My Solution

```python
def find_longest(string):
    return max(len(word) for word in string.split(" "))
```

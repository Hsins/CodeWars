# Isograms

## Information

- KYU: 7
- Link: [Isograms](https://www.codewars.com/kata/isograms/train/python)

## Description:

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

```
is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
```

## My Solution

```python
def is_isogram(string):
    return len(set(string.lower())) == len(string)
```

## Lambda Solutions

```python
is_isogram = lambda string: len(set(string.lower())) == len(string)
```


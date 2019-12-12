# Sort by Last Char

## Information

- KYU: 7
- Link: [Sort by Last Char](https://www.codewars.com/kata/find-the-integral/train/python)

## Description:

Given a string of words (x), you need to return an array of the words, sorted alphabetically by the final character in each.

If two words have the same last letter, they returned array should show them in the order they appeared in the given string.

All inputs will be valid.

## My Solution

```python
def last(x):
    return sorted(x.split(' '), key=lambda word: word[-1])
```

## Clever Solution

```python
def last(s):
    return sorted(s.split(), key=itemgetter(-1))
```

## References

- [Python Document | Sorting HOW TO](https://docs.python.org/3/howto/sorting.html#sorting-how-to)
- [Python Document | `operator.itemgetter(item)`](https://docs.python.org/3/library/operator.html#operator.itemgetter)
- [Python Document | Operator Module Functions](https://docs.python.org/3/howto/sorting.html#operator-module-functions)
- [stackoverflow | Python: How to Sort List by Last Character of String](https://stackoverflow.com/questions/31306951/python-how-to-sort-list-by-last-character-of-string)
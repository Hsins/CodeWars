# Santa's Naughty List

## Information

- KYU: 7
- Link: [Santa's Naughty List](https://www.codewars.com/kata/santas-naughty-list/train/python)

## Description:

Christmas is coming, and Santa has a long list to go through, to find who deserves presents for the big day. Go through a list of children, and return a list containing every child who appeared on Santa's list. Do not add any child more than once. Output should be sorted.

Comparison should be case sensitive and the returned list should contain only one copy of each name: `"Sam"` and `"sam"` are different, but `"sAm"` and `"sAm"` are not.

## My Solution

```python
def find_children(santas_list, children):
    return sorted(set(santas_list) & set(children))
```

## Clever Solutions

```python
def find_children(santas_list, children):
    return sorted(list(set(santas_list).intersection(children)))
```

## Lambda Solutions

```python
find_children = lambda santas_list, children: sorted(set(santas_list) & set(children))
```

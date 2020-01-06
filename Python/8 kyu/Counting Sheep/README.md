# Counting Sheep

## Information

- KYU: 8
- Link: [Counting Sheep](https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python)

## Description:

Consider an array of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

**Example**:

```
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

The correct answer would be 17.
```

**Hint**: Don't forget to check for bad values like null/undefined

## My Solution

```python
def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)
```

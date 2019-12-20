# Grasshopper - Messi Goals Function

## Information

- KYU: 8
- Link: [Grasshopper - Messi Goals Function](https://www.codewars.com/kata/grasshopper-messi-goals-function/train/python)

## Description:

[Messi](https://en.wikipedia.org/wiki/Lionel_Messi) is a soccer player with goals in three leagues:

- LaLiga
- Copa del Rey
- Champions

Complete the function to return his total number of goals in all three leagues.

**Note**: the input will always be valid.

**Example**:

```
5, 10, 2  -->  17
```

## My Solution

```python
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague
```

## Clever Solutions

```python
def goals(*args):
    return sum(args)
```

## Lambda Solutions

```python
goals = lambda *args: sum(args)
```
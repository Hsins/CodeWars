# 101 Dalmatians - Squash the Bugs, Not the Dogs

## Information

- KYU: 8
- Link: [101 Dalmatians - Squash the Bugs, Not the Dogs](https://www.codewars.com/kata/101-dalmatians-squash-the-bugs-not-the-dogs/train/python)

## Description:

Your friend has been out shopping for puppies (what a time to be alive!)... He arrives back with multiple dogs, and you simply do not know how to respond!

By repairing the function provided, you will find out exactly how you should respond, depending on the number of dogs he has.

The number of dogs will always be a number and there will always be at least 1 dog.

## My Solution

```python
def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    if n <= 10:
        return dogs[0]
    elif n <= 50:
        return dogs[1]
    elif n == 101:
        return dogs[3]
    else:
        return dogs[2]
```

## Clever Solutions

```python
def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    return dogs[0] if n <= 10 else dogs[1] if n <=50 else dogs[3] if n == 101 else dogs[2]
```

```python
responses = [
  (lambda n: n < 11, "Hardly any"),
  (lambda n: n < 51, "More than a handful!"),
  (lambda n: n == 101, "101 DALMATIONS!!!"),
  (lambda n: True, "Woah that's a lot of dogs!")
]

how_many_dalmatians = lambda n: next(r for p, r in responses if p(n))
```

```python
DOGS = ((100, '101 DALMATIONS!!!'), (50, 'Woah that\'s a lot of dogs!'),
        (10, 'More than a handful!'))


def how_many_dalmatians(n):
    return next((msg for dogs, msg in DOGS if n > dogs), 'Hardly any')
```

## Lambda Solutions

```python
how_many_dalmatians = lambda n: ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"][sum([n>10, n>50, n>=101])]
```
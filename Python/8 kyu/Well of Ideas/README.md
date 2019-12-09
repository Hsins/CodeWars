# Well of Ideas

## Information

- KYU: 8
- Link: [Well of Ideas](https://www.codewars.com/kata/well-of-ideas-easy-version/train/python)

## Description:

For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array `x` for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

## My Solution

```python
def well(x):
    count = x.count('good')

    if count == 0:
        return 'Fail!'
    elif count > 2:
        return 'I smell a series!'
    else:
        return 'Publish!'
```

## Clever Solutions

```python
def well(x):
    count = x.count('good')
    return 'I smell a series!' if count > 2 else 'Publish!' if count else 'Fail!'
```
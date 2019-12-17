# Swap Values

## Information

- KYU: 8
- Link: [Swap Values](https://www.codewars.com/kata/5-without-numbers/train/python)

## Description:

I would like to be able to pass an array with two elements to my `swapValues` function to swap the values. However it appears that the values aren't changing.

Can you figure out what's wrong here?

## My Solution

```python
def swap_values(args):
    args[0], args[1] = args[1], args[0]
```

## Clever Solutions

```python
def swap_values(args):
    args.extend([args.pop(),args.pop()])
```

```python
def swap_values(args):
    tmp = args[0]
    args[0] = args[1]
    args[1] = tmp
```

## Lambda Solutions

```python
swap_values = lambda args: args.reverse()
```
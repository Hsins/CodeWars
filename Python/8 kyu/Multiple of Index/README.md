# Multiple of Index

## Information

- KYU: 8
- Link: [Multiple of Index](https://www.codewars.com/kata/multiple-of-index/train/python)

## Description:

Return a new array consisting of elements which are multiple of their own index in input array (length > 1).

Some cases:

```
[22, -6, 32, 82, 9, 25] =>  [-6, 32, 25]
[68, -1, 1, -7, 10, 10] => [-1, 10]
[-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68] => [-85, 72, 0, 68]
```


## My Solution

```python
def multiple_of_index(arr):
    result = []
    for idx, num in enumerate(arr):
        if idx == 0:
            continue
        if num % idx == 0:
            result.append(num)
    
    return result
```

## Clever Solutions

```python
def multiple_of_index(arr):
    return [num for idx, num in enumerate(arr) if idx and num % idx == 0]
```

## Lambda Solutions

```python
multiple_of_index = lambda arr: [num for idx, num in enumerate(arr) if idx and num % idx == 0]
```
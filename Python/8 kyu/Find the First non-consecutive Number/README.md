# Find the First non-consecutive Number

## Information

- KYU: 8
- Link: [Find the First non-consecutive Number](https://www.codewars.com/kata/find-the-first-non-consecutive-number/train/python)

## Description:

Your task is to find the first element of an array that is not consecutive.

E.g. If we have an array `[1,2,3,4,6,7,8]` then `1` then `2` then `3` then `4` are all consecutive but `6` is not, so that's the first non-consecutive number.

If the whole array is consecutive then return `null` or `Nothing`.

The array will always have at least `2` elements and all elements will be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive or negative and the first non-consecutive could be either too!

If you like this Kata, maybe try this one next: https://www.codewars.com/kata/represent-array-of-numbers-as-ranges

- Can you write a solution that will return null for both [] and [ x ] though? (This is not tested, but you can write your own example test.)

## My Solution

```python
def first_non_consecutive(arr):
    for idx, num in enumerate(arr): 
        if num - arr[idx-1] != 1 and idx: 
            return(num)
    return None
```

## Clever Solutions

```python
def first_non_consecutive(arr):
    return next((j for i, j in zip(arr, arr[1:]) if i + 1 != j), None)
```

透過內置函數 `zip()` 函數將陣列個別元素兩兩進行打包，並逐一比較元素對是否差值為一。

## Lambda Solutions

```python
first_non_consecutive = lambda arr: min([num for idx, num in enumerate(arr) if idx and num != arr[idx-1]+1] or [None])
```
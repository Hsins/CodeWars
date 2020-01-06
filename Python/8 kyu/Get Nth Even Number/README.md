# Get Nth Even Number

## Information

- KYU: 8
- Link: [Get Nth Even Number](https://www.codewars.com/kata/get-nth-even-number/train/python)

## Description:

Return the Nth Even Number

```
nthEven(1)          //=> 0, the first even number is 0
nthEven(3)          //=> 4, the 3rd even number is 4 (0, 2, 4)

nthEven(100)        //=> 198
nthEven(1298734)    //=> 2597466
```

The input will not be 0.

## My Solution

```python
def nth_even(n):
    return 2 * (n - 1)
```

## Clever Solutions

```python
def nth_even(n):
    return ~(-n) << 1
```

在 Python 中的波浪操作符（tilde operator） `~` 是對數字進行按位取反的操作（包括表示正負號的符號位）。有以下幾點值得注意：

- 若對正數進行按位取反，各位取反變為負數，顯示時轉為補數
- 若對負數進行按位取反，本身需要先轉換為補數（符號位不變，各位取反再加一），再對補數進行各位取反


## Lambda Solutions

```python
nth_even = lambda n: 2 * (n - 1)
```
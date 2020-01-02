# Find the Odd Int

## Information

- KYU: 6
- Link: [Find the Odd Int](https://www.codewars.com/kata/find-the-odd-int/train/python)

## Description:

Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

## My Solution

```python
def find_it(seq):
    result = 0
    for num in seq:
        result ^= num
    return result
```

在位元運算中，互斥或（XOR）運算的真值表如下：

| A | B | A xor B |
| :--: | :--: | :--: |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

- 當 0 與任意數進行 XOR 運算之後會得到任意數本身
- 當任意數與本身進行 XOR 運算之後會得到零

由於 XOR 運算滿足結合律與交換律，最後得到的結果便是落單（出現次數為奇數次）的數字。

## References

- [Wikipedia | Exclusive or](https://www.wikiwand.com/en/Exclusive_or)
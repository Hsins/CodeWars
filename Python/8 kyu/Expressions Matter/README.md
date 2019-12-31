# Expressions Matter

## Information

- KYU: 8
- Link: [Expressions Matter](https://www.codewars.com/kata/expressions-matter/train/python)

## Description:

Given three integers `a` ,`b` ,`c`, return the largest number obtained after inserting the following operators and brackets: `+`, `*`, `()`.

With the numbers are `1`, `2` and `3` , here are some ways of placing signs and brackets:

```
1 * (2 + 3) = 5
1 * 2 * 3 = 6
1 + 2 * 3 = 7
(1 + 2) * 3 = 9
```

So the maximum value that you can obtain is 9.

**Notes**:

- The numbers are always positive.
- The numbers are in the range (1  ≤  a, b, c  ≤  10).
- You can use the same operation more than once.
- It's not necessary to place all the signs and brackets.
- Repetition in numbers may occur.
- You cannot swap the operands. For instance, in the given example you cannot get expression (1 + 3) * 2 = 8.

**Examples**:

```
expressionsMatter(1,2,3)  ==>  return 9
Explanation:
After placing signs and brackets, the Maximum value obtained from the expression (1+2) * 3 = 9.

expressionsMatter(1,1,1)  ==>  return 3
Explanation:
After placing signs, the Maximum value obtained from the expression is 1 + 1 + 1 = 3.

expressionsMatter(9,1,1)  ==>  return 18
Explanation:
After placing signs and brackets, the Maximum value obtained from the expression is 9 * (1+1) = 18.
```

## My Solution

```python
def expression_matter(a, b, c):
    return max(a * b * c, a + b + c, (a + b) * c, a * (b + c))
```

實際上應該會有六種運算組合，但其中兩種可以根據簡單的數學不等式得證必定小於等於其他四種運算組合。
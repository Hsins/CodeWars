# Do I get a bonus?

## Information

- KYU: 8
- Link: [Do I get a bonus?](https://www.codewars.com/kata/56f6ad906b88de513f000d96/)

## Description:

It's bonus time in the big city! The fatcats are rubbing their paws in anticipation... but who is going to make the most money?

Build a function that takes in two arguments (salary, bonus). Salary will be an integer, and bonus a boolean.

If bonus is true, the salary should be multiplied by 10. If bonus is false, the fatcat did not make enough money and must receive only his stated salary.

Return the total figure the individual will receive as a string prefixed with "£" (= `"\u00A3"`, JS, Go, and Java), "$" (C#, C++, Ruby, Clojure, Elixir, PHP and Python, Haskell, Lua) or "¥" (Rust).

## My Solution

```python
def bonus_time(salary, bonus):
    return "${}".format(salary * 10 if bonus else salary)
```

## Clever Solutions

```python
def bonus_time(salary, bonus):
    return '$' + str(salary * [1,10][bonus])
```

在 Python 中，布林值 `True` 轉換成整數時為 `1`，而 `False` 轉換成整數為 `0`。這個解法利用這個概念，將要乘上的數值放在陣列中，並將布林值作為索引值傳入取值。
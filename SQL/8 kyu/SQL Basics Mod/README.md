# SQL Basics: Mod

## Information

- KYU: 8
- Link: [SQL Basics: Mod](https://www.codewars.com/kata/sql-basics-mod/train/sql)

## Description:

Given the following table `decimals`:

**decimals table schema**:

- id
- number1
- number2

Return a table with one column (`mod`) which is the output of number1 modulus number2.

## My Solution

```sql
SELECT
    MOD(number1, number2) AS mod
FROM
    decimals;
```

## Clever Solutions

```sql
SELECT
    number1 % numer2 AS mod
FROM
    decimals
```
# Easy SQL Ordering

## Information

- KYU: 8
- Link: [Easy SQL - Ordering](https://www.codewars.com/kata/easy-sql-ordering/train/sql)

## Description:

Your task is to sort the information in the provided table 'companies' by number of employees (high to low). Returned table should be in the same format as provided:

**companies table schema**:

- id
- ceo
- motto
- employees

Solution should use pure SQL. Ruby is only used in test cases.

## My Solution

```sql
SELECT
    *
FROM
    companies
ORDER BY
    employees DESC;
```

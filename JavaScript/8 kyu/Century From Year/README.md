# Century From Year

## Information

- KYU: 8
- Link: [Century From Year](https://www.codewars.com/kata/century-from-year/train/javascript)

## Description:

The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.

Given a year, return the century it is in.

**Examples**:

```
centuryFromYear(1705)  returns (18)
centuryFromYear(1900)  returns (19)
centuryFromYear(1601)  returns (17)
centuryFromYear(2000)  returns (20)
```

Hope you enjoy it .. Awaiting for Best Practice Codes

Enjoy Learning !!!

## My Solution

```javascript
function century(year) {
  return Math.ceil(year / 100);
}
```

```javascript
const century = year => Math.ceil(year / 100);
```

## Clever Solutions

```javascript
const century = year => (year + 99) / 100 | 0;
```

操作符 `|` 對浮點數進行或（OR）運算，會截斷小數部份並將浮點數轉換為整數，運算速度上比起 `Math.floor()` 要 [稍快](https://jsperf.com/or-vs-floor/2) 一點，但有以下要注意的：

- 只能作用到 32 位有符號整數
- 對 `NaN` 的操作結果與 `Math.floor()` 不同
  - `Math.floor(NaN) === NaN`
  - `(NaN | 0) === 0`

## References

- [stackoverflow | ](https://stackoverflow.com/questions/7487977/using-bitwise-or-0-to-floor-a-number)
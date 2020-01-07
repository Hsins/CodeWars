# Century From Year

## Information

- KYU: 8
- Link: [Century From Year](https://www.codewars.com/kata/century-from-year/train/cpp)

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

```cpp
constexpr int centuryFromYear(int year) { return (year + 99) / 100; }
```

## Clever Solutions

```cpp
constexpr int centuryFromYear(int year) { return (year % 100) ? (year / 100) + 1 : (year / 100); }
```

```cpp
#include <cmath>

constexpr float centuryFromYear(float year) { return std::ceil(year / 100); }
```
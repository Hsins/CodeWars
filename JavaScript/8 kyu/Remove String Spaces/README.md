# Remove String Spaces

## Information

- KYU: 8
- Link: [Remove String Spaces](https://www.codewars.com/kata/remove-string-spaces/train/javascript)

## Description:

Simple, remove the spaces from the string, then return the resultant string.

## My Solution

```javascript
const noSpace = string => string.replace(/\s/g, '');
```

## Clever Solutions

```javascript
const noSpace = string => string.split(' ').join('').trim();
```
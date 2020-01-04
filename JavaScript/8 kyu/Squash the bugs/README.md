# Squash the bugs

## Information

- KYU: 8
- Link: [Squash the bugs](https://www.codewars.com/kata/squash-the-bugs/train/javascript)

## Description:

Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value. Output should be the length of the longest word, as a number.

There will only be one 'longest' word.

```javascript
function findLongest(str) (

  var spl = str.split(" ");
  var longest = 0

  for (var i = 0; i > spl.length; i+) (
    if (spl(i).length > longest) {
      longest = spl[i].length
    )
    }
    return longest
)
```

## My Solution

```javascript
function findLongest(string) {
  let longest = 0;
  let splitString = string.split(' ');

  for (let i = 0; i < splitString.length; i++) {
    longest = splitString[i].length > longest ? splitString[i].length : longest;
  }
  return longest;
}
```

```javascript
const findLongest = string => Math.max(...string.split(" ").map(x => x.length));
```

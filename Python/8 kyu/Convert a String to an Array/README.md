# Convert a String to an Array

## Information

- KYU: 8
- Link: [Convert a String to an Array](https://www.codewars.com/kata/convert-a-string-to-an-array/train/python)

## Description:

Write a function to split a string and convert it into an array of words. For example:

```
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
```

## My Solution

```python
def string_to_array(s):
    return s.split(" ")
```

## Lambda Solutions

```python
string_to_array = lambda x: x.split(" ")
```

# Alphabetical Addition

## Information

- KYU: 7
- Link: [Alphabetical Addition](https://www.codewars.com/kata/alphabetical-addition/train/python)

## Description:

Your task is to add up letters to one letter.

The function will be given a variable amount of arguments, each one being a letter to add.

**Notes**:

Letters will always be lowercase.
Letters can overflow (see second to last example of the description)
If no letters are given, the function should return 'z'

**Examples**:

```
add_letters('a', 'b', 'c') = 'f'
add_letters('a', 'b') = 'c'
add_letters('z') = 'z'
add_letters('z', 'a') = 'a'
add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
add_letters() = 'z'
```

**Hint**:

Start by converting the letters to numbers, a => 1, b => 2, etc. Add them up. Think about the overflow yourself. Once that's done, convert it back to a letter.

## My Solution

```python
def add_letters(*letters):
    sum_letter = sum([ord(char) - 96 for char in letters]) % 26
    return chr(sum_letter + 96) if sum_letter else 'z'
```

## Clever Solutions

```python
def add_letters(*letters):
    return chr((sum(ord(char) - 96 for char in letters) - 1) % 26 + 97)
```

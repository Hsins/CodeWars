# Grasshopper - Personalized Message

## Information

- KYU: 8
- Link: [Grasshopper - Personalized Message](https://www.codewars.com/kata/grasshopper-personalized-message/train/python)

## Description:

Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:

| case | return |
| :--: | :-- |
| name equals owner | `'Hello boss'` |
| otherwise | `'Hello guest'` |

## My Solution

```python
def greet(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'
```

## Clever Solutions

```python
def greet(name, owner):
    return "Hello {}".format("boss" if name == owner else "guest")
```

```python
def greet(name, owner):
    return 'Hello '+ ['guest', 'boss'][name == owner]
```

## Lambda Solutions

```python
greet = lambda name, owner: "Hello {}".format(["guest", "boss"][name == owner])
```
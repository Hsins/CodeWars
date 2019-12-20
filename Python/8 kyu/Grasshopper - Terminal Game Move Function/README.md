# Grasshopper - Terminal Game Move Function

## Information

- KYU: 8
- Link: [Grasshopper - Terminal Game Move Function](https://www.codewars.com/kata/grasshopper-terminal-game-move-function/train/python)

## Description:

Terminal game move function
In this game, the hero moves from left to right. The player rolls the dice and moves the number of spaces indicated by the dice **two times**.

Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.

```
Example:
move(3, 6) should equal 15
```

## My Solution

```python
def move(position, roll):
    return position + 2 * roll
```

## Lambda Solutions

```python
move = lambda position, roll: position + 2 * roll
```
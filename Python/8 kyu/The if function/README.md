# The if function

## Information

- KYU: 8
- Link: [The if function](https://www.codewars.com/kata/the-if-function/train/python)

## Description:

Who likes keywords? Nobody likes keywords, so why use them?

You know what keyword I use too much? `if`! We should make a function called `_if`, with its **arguments as a logical test and two functions/lambdas where the first function is executed if the boolean is true, and the second if it's false**, like an if/else statement, so that we don't have to mess around with those nasty keywords! Even so, **It should support truthy/falsy types** just like the keyword.

**Example**:

```python
def truthy(): print("True")
def falsey(): print("False")
_if(True, truthy, falsey)
# prints 'True' to the console
```

## My Solution

```python
def _if(bool, func1, func2):
    return func1() if bool else func2()
```

## Lambda Solutions

```python
lambda bool, func1, func2: (bool and func1 or func2)()
```
# The Lamp: Revisited

## Information

- KYU: 6
- Link: [The Lamp: Revisited](https://www.codewars.com/kata/the-lamp-revisited/train/python)

## Description:

Define a class called `Lamp`. It will have a string attribute for `color` and boolean attribute, `on`, that will refer to whether the lamp is on or not. Define your class constructor with a parameter for color and assign `on` as `false` on initialize.

Give the lamp an instance method called `toggle_switch` that will switch the value of the `on` attribute.

Define another instance method called `state` that will return `"The lamp is on."` if it's on and `"The lamp is off."` otherwise.

## My Solution

```python
class Lamp(object):
    def __init__(self, color=None, on=False):
        self.color = color
        self.on = on

    def toggle_switch(self):
        # self.on ^= 1
        self.on = not self.on

    def state(self):
        return "The lamp is {}.".format("on" if self.on else "off")
```

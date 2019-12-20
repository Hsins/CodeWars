# I Love You, A Little, A Lot, Passionately... Not At All

## Information

- KYU: 8
- Link: [I Love You, A Little, A Lot, Passionately... Not At All](https://www.codewars.com/kata/i-love-you-a-little-a-lot-passionately-dot-dot-dot-not-at-all/train/python)

## Description:

Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:

- I love you
- a little
- a lot
- passionately
- madly
- not at all

When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal in this kata is to determine which phrase the girls would say for a flower of a given number of petals, where `nb_petals` > 0.

## My Solution

```python
def how_much_i_love_you(nb_petals):
    return ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all'][nb_petals % 6 - 1]
```

## Clever Solutions

```python
def how_much_i_love_you(nb_petals):
    words = {1: 'I love you', 2: 'a little', 3: 'a lot', 4: 'passionately', 5: 'madly', 0: 'not at all'}
    return words[nb_petals%6]
```
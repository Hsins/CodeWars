# A Strange Trip to the Market

## Information

- KYU: 8
- Link: [A Strange Trip to the Market](https://www.codewars.com/kata/a-strange-trip-to-the-market/train/python)

## Description:

You're on your way to the market when you hear beautiful music coming from a nearby street performer. The notes come together like you wouln't believe as the musician puts together patterns of tunes. As you wonder what kind of algorithm you could use to shift octaves by 8 pitches or something silly like that, it dawns on you that you have been watching the musician for some 10 odd minutes. You ask, "How much do people normally tip for something like this?" The artist looks up. "Its always gonna be about tree fiddy."

It was then that you realize the musician was a 400 foot tall beast from the paleolithic era. The Loch Ness Monster almost tricked you!

There are only 2 guaranteed ways to tell if you are speaking to The Loch Ness Monster: A.) It is a 400 foot tall beast from the paleolithic era B.) It will ask you for tree fiddy

Since Nessie is a master of disguise, the only way accurately tell is to look for the phrase "tree fiddy". Since you are tired of being grifted by this monster, the time has come to code a solution for finding The Loch Ness Monster. Note: It can also be written as 3.50 or three fifty.

## My Solution

```python
def is_lock_ness_monster(string):
    words = ['tree fiddy', '3.50', 'three fifty']
    return True if any(word in string for word in words) else False
```

## Clever Solutions

```python
import re

def is_lock_ness_monster(string):
    return bool(re.search(r"3\.50|tree fiddy|three fifty", string))
```

## Lambda Solutions

```python
is_lock_ness_monster=lambda string: any(_ in string for _ in['3.50','tree fiddy','three fifty'])
```

## References

- [stackoverflow | Check if multiple strings exist in another string](https://stackoverflow.com/questions/3389574/check-if-multiple-strings-exist-in-another-string)
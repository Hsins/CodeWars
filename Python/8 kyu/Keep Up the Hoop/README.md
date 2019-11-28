# Keep Up the Hoop

## Information

- KYU: 8
- Link: [Keep Up the Hoop](https://www.codewars.com/kata/keep-up-the-hoop/train/python)

## Description:

Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him.

Write a program where Alex can input (`n`) how many times the hoop goes round and it will return him an encouraging message :)

- If Alex gets 10 or more hoops, return the string `"Great, now move on to tricks"`.
- If he doesn't get 10 hoops, return the string `"Keep at it until you get it"`.

## My Solution

```python
def hoop_count(n):
    return "Keep at it until you get it" if n < 10 else "Great, now move on to tricks"
```

## Lambda Solutions

```python
hoop_count = lambda n: ["Keep at it until you get it", "Great, now move on to tricks"][n >= 10]
```
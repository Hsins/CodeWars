# Calculate BMI

## Information

- KYU: 8
- Link: [Calculate BMI](https://www.codewars.com/kata/calculate-bmi/train/python)

## Description:

Write function bmi that calculates body mass index (bmi = weight / height ^ 2).

- if bmi <= 18.5 return `"Underweight"`
- if bmi <= 25.0 return `"Normal"`
- if bmi <= 30.0 return `"Overweight"`
- if bmi > 30 return `"Obese"`

## My Solution

```python
def bmi(weight, height):
    bmi = weight / (height**2)

    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"
```

## Clever Solutions

```python
def bmi(weight, height):
    bmi = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(bmi > 30) + (bmi > 25) + (bmi > 18.5)]
```

這個方法有點巧妙，是利用了布林值對應整數值的概念。舉例來說當 `bmi = 27` 時：

```
  (b > 30) + (b > 25) + (b > 18.5)
=  False   +  True    +  True
=    0     +    1     +    1
=    2
```

## Lambda Solutions

```python
bmi = lambda w, h: (lambda b=w/h**2: ["Underweight", "Normal", "Overweight", "Obese"][(18.5 < b) + (25 < b) + (30 < b)])()
```
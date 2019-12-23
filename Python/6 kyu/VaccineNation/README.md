# VaccineNation

## Information

- KYU: 6
- Link: [VaccineNation](https://www.codewars.com/kata/vaccinenation/train/python)

## Description:

Vaccinations for children under 5

You have been put in charge of administrating vaccinations for children in your local area. Write a function that will generate a list of vaccines for each child presented for vaccination, based on the child's age and vaccination history, and the month of the year.

The function takes three parameters: `age`, `status` and `month`

- The parameter `age` will be given in weeks up to 16 weeks, and thereafter in months. You can assume that children presented will be scheduled for vaccination (eg '16 weeks', '12 months' etc).
- The parameter `status` indicates if the child has missed a scheduled vaccination, and the argument will be a string that says 'up-to-date', or a scheduled stage (eg '8 weeks') that has been missed, in which case you need to add any missing shots to the list. Only one missed vaccination stage will be passed in per function call.
- If the month is 'september', 'october' or 'november' add 'offer fluVaccine' to the list.
- Make sure there are no duplicates in the returned list, and sort it alphabetically.

**Examples**:

```
input     ('12 weeks', 'up-to-date', 'december')
output    ['fiveInOne', 'rotavirus']

input     ('12 months', '16 weeks', 'june')
output     ['fiveInOne', 'hibMenC', 'measlesMumpsRubella', 'meningitisB', 'pneumococcal']

input     ('40 months', '12 months', 'october')
output    ['hibMenC', 'measlesMumpsRubella', 'meningitisB', 'offer fluVaccine', 'preSchoolBooster']
```

To save you typing it up, here is the vaccinations list

```
fiveInOne : ['8 weeks', '12 weeks', '16 weeks'],
// Protects against: diphtheria, tetanus, whooping cough, polio and Hib (Haemophilus influenzae type b)
pneumococcal : ['8 weeks', '16 weeks'],
// Protects against: some types of pneumococcal infection
rotavirus : ['8 weeks', '12 weeks'],
// Protects against: rotavirus infection, a common cause of childhood diarrhoea and sickness
meningitisB : ['8 weeks', '16 weeks', '12 months'],
// Protects against: meningitis caused by meningococcal type B bacteria
hibMenC : ['12 months'],
// Protects against: Haemophilus influenzae type b (Hib), meningitis caused by meningococcal group C bacteria
measlesMumpsRubella : ['12 months', '40 months'],
// Protects against: measles, mumps and rubella
fluVaccine : ['september','october','november'],
// Given at: annually in Sept/Oct
preSchoolBooster : ['40 months']
// Protects against: diphtheria, tetanus, whooping cough and polio
```

## My Solution

```python
def vaccine_list(age, status, month):
    vaccins = {
        "fiveInOne":            ['8 weeks', '12 weeks', '16 weeks'],
        "pneumococcal":         ['8 weeks', '16 weeks'],
        "rotavirus":            ['8 weeks', '12 weeks'],
        "meningitisB":          ['8 weeks', '16 weeks', '12 months'],
        "hibMenC":              ['12 months'],
        "measlesMumpsRubella":  ['12 months', '40 months'],
        "preSchoolBooster":     ['40 months'],
        "offer fluVaccine":     ['september', 'october', 'november']
    }

    result = set()
    for vaccine in vaccins:
        if age in vaccins[vaccine] or month in vaccins[vaccine] or status in vaccins[vaccine]:
            result.add(vaccine)

    return sorted(result)
```

## Clever Solutions

```python
vaccins = {
    'fiveInOne':           ('8 weeks','12 weeks','16 weeks'),
    'pneumococcal':        ('8 weeks','16 weeks'),
    'rotavirus':           ('8 weeks','12 weeks'),
    'meningitisB':         ('8 weeks','16 weeks','12 months'),
    'hibMenC':             ('12 months',),
    'measlesMumpsRubella': ('12 months','40 months'),
    'preSchoolBooster':    ('40 months',)
    'offer fluVaccine':    ('september','october','november'),
}

vaccine_list = lambda *args: sorted({k for i in args for k, l in vaccins.items() if i in l if i != 'up-to-date'})
```

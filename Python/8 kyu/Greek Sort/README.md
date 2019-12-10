# Greek Sort

## Information

- KYU: 8
- Link: [Greek Sort](https://www.codewars.com/kata/greek-sort/train/python)

## Description:

Write a comparator for a list of phonetic words for the letters of the [greek alphabet](https://www.wikiwand.com/en/Greek_alphabet).

A comparator is:

> a custom comparison function of two arguments (iterable elements) which should return a negative, zero or positive number depending on whether the first argument is considered smaller than, equal to, or larger than the second argument
> (source: https://docs.python.org/2/library/functions.html#sorted)

The greek alphabet is preloded for you as `greek_alphabet`:

```
greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')
```

Examples:

```
greek_comparator('alpha', 'beta')   <  0
greek_comparator('psi', 'psi')      == 0
greek_comparator('upsilon', 'rho')  >  0
```

## My Solution

```python
def two_sort(array):
    word = sorted(array)[0]
    return "***".join(word)
```

## Clever Solutions

```python
def two_sort(array):
    return '***'.join(min(array))
```

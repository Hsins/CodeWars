# Regex Password Validation

## Information

- KYU: 5
- Link: [Regex Password Validation](https://www.codewars.com/kata/calculating-with-functions/train/python)

## Description:

You need to write regex that will validate a password to make sure it meets the following criteria:

- At least six characters long
- contains a lowercase letter
- contains an uppercase letter
- contains a number

Valid passwords will only be alphanumeric characters.

## My Solution

```python
regex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[A-Za-z0-9]{6,}$"

"""
^               # start letter
(?=.*?[A-Z])    # at least one uppercase letter
(?=.*?[a-z])    # at least one lowercase letter
(?=.*?[0-9])    # at least one number
[A-Za-z0-9]     # only alphanumber
{6,}            # at least 6 characters
$               # end letter
"""
```

## References

- [stackoverflow | Regex Password Validation - Codewars(https://stackoverflow.com/questions/29465214/regex-password-validation-codewars)
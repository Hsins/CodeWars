# Extract the Domain Name From a URL

## Information

- KYU: 5
- Link: [Extract the Domain Name From a URL](https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1/train/python)

## Description:

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

**Example**:

```
domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
```

## My Solution

```python
import re


def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<domain>[\w-]+)\.', url).group('domain')

"""
(https?://)?            # matches http://, https:// or nothing
(www\d?\.)?             # matches www, www1, www2, ... or nothing
(?P<domain>[\w-]+)\.    # create a match group named [domain]
"""
```

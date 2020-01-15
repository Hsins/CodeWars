# [5 kyu] Extract the Domain Name From a URL
#
# Author:   Hsins
# Date:     2020/01/15
import re


def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<domain>[\w-]+)\.', url).group('domain')

"""
(https?://)?            # matches http://, https:// or nothing
(www\d?\.)?             # matches www, www1, www2, ... or nothing
(?P<domain>[\w-]+)\.    # create a match group named [domain]
"""
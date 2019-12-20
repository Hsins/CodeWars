# [8 kyu] Regexp Basics - Is It a Digit?
#
# Author:   Hsins
# Date:     2019/12/20
import re


def is_digit(n):
    return bool(re.fullmatch(r'^[0-9]$', n))

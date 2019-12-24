# [8 kyu] Simple Validation of a Username with Regex
#
# Author:   Hsins
# Date:     2019/12/24
import re


def validate_usr(username):
    pattern = re.compile("^[a-z0-9_]{4,16}$")
    return bool(pattern.match(username))

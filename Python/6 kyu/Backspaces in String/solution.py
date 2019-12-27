# [6 kyu] Backspaces in String
#
# Author:   Hsins
# Date:     2019/12/27


def clean_string(string):
    result = ""

    for char in string:
        if char == "#":
            result = result[:-1]
        else:
            result += char

    return result

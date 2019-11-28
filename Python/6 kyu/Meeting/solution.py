# [6 kyu] Meeting
#
# Author:   Hsins
# Date:     2019/11/28


def meeting(s):
    names = []
    friends = ""

    for _ in s.upper().split(";"):
        names.append(_.split(":")[::-1])

    for name in sorted(names):
        friends += '({}, {})'.format(name[0], name[1])

    return friends

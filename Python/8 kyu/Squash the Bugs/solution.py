# [8 kyu] Squash the Bugs
#
# Author:   Hsins
# Date:     2020/01/02


def find_longest(string):
    return max(len(word) for word in string.split(" "))

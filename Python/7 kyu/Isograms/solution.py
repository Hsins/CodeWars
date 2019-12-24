# [7 kyu] Isograms
#
# Author:   Hsins
# Date:     2019/12/24


def is_isogram(string):
    return len(set(string.lower())) == len(string)

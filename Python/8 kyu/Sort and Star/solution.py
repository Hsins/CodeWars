# [8 kyu] Double Char
#
# Author:   Hsins
# Date:     2019/11/28


def two_sort(array):
    word = sorted(array)[0]
    return "".join(c + '***' for c in word)[0:-3]

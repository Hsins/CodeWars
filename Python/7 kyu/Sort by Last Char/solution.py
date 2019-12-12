# [7 kyu] Sort by Last Char
#
# Author:   Hsins
# Date:     2019/12/12


def last(x):
    return sorted(x.split(' '), key=lambda word: word[-1])

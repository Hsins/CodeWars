# [7 kyu] Find All Occurrences of An Element in An Array
#
# Author:   Hsins
# Date:     2020/01/02


def find_all(array, n):
    return [idx for idx, num in enumerate(array) if num == n]

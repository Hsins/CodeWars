# [8 kyu] Merging Sorted Integer Arrays (Without Duplicates)
#
# Author:   Hsins
# Date:     2019/12/11


def merge_arrays(first, second):
    return sorted(set(first + second))

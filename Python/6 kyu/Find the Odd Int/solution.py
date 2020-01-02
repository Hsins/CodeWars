# [6 kyu] Find the Odd Int
#
# Author:   Hsins
# Date:     2020/01/02


def find_it(seq):
    result = 0
    for num in seq:
        result ^= num
    return result

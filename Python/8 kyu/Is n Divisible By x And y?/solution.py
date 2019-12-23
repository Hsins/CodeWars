# [8 kyu] Is n Divisible By x And y?
#
# Author:   Hsins
# Date:     2019/12/23


def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0

# [7 kyu] Summing a Number's Digits
#
# Author:   Hsins
# Date:     2019/12/23


def sum_digits(number):
    return sum(map(int, str(abs(number))))

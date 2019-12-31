# [7 kyu] Descending Order
#
# Author:   Hsins
# Date:     2019/12/31


def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))

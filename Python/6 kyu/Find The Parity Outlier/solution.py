# [6 kyu] Find The Parity Outlier
#
# Author:   Hsins
# Date:     2019/12/28


def find_outlier(integers):
    is_odd = True if (integers[0] % 2 + integers[1] % 2 + integers[2] % 2) < 2 else False

    if is_odd:
        for integer in integers:
            if integer % 2:
                return integer
    else:
        for integer in integers:
            if not integer % 2:
                return integer

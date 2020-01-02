# [7 kyu] Square Every Digit
#
# Author:   Hsins
# Date:     2020/01/02


def square_digits(num):
    return int(''.join(str(int(_)**2) for _ in str(num)))

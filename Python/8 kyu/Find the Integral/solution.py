# [8 kyu] Find the Integral
#
# Author:   Hsins
# Date:     2019/12/12


def integrate(coefficient, exponent):
    return "{}x^{}".format(coefficient // (exponent + 1), exponent + 1)

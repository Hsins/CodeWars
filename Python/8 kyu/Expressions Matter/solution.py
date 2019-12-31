# [8 kyu] Expressions Matter
#
# Author:   Hsins
# Date:     2019/12/31


def expression_matter(a, b, c):
    return max(a * b * c, a + b + c, (a + b) * c, a * (b + c))

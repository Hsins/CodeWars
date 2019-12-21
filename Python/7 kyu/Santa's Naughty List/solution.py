# [7 kyu] Santa's Naughty List
#
# Author:   Hsins
# Date:     2019/12/21


def find_children(santas_list, children):
    return sorted(set(santas_list) & set(children))

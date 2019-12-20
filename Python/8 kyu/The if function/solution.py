# [8 kyu] The if function
#
# Author:   Hsins
# Date:     2019/12/20


def _if(bool, func1, func2):
    return func1() if bool else func2()

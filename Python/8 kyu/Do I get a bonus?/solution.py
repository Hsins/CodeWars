# [8 kyu] Do I get a bonus?
#
# Author:   Hsins
# Date:     2019/11/28


def bonus_time(salary, bonus):
    result = '${}'.format(salary * 10 if bonus else salary)
    return result

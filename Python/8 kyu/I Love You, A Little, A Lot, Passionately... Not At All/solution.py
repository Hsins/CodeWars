# [8 kyu] I Love You, A Little, A Lot, Passionately... Not At All
#
# Author:   Hsins
# Date:     2019/12/20


def how_much_i_love_you(nb_petals):
    return ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all'][nb_petals % 6 - 1]

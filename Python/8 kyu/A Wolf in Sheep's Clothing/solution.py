# [8 kyu] A Wolf in Sheep's Clothing
#
# Author:   Hsins
# Date:     2019/12/06


def warn_the_sheep(queue):
    queue.reverse()
    return "Pls go away and stop eating my sheep" if queue.index('wolf') == 0 else "Oi! Sheep number {}! You are about to be eaten by a wolf!".format(queue.index('wolf'))

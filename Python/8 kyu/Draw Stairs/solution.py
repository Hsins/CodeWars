# [8 kyu] Draw Stairs
#
# Author:   Hsins
# Date:     2019/12/03


def draw_stairs(n):
    return('\n'.join(i * ' ' + 'I' for i in range(n)))

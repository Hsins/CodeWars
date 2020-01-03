# [6 kyu] Look and Say Numbers
#
# Author:   Hsins
# Date:     2020/01/03
from itertools import groupby


def look_and_say(data='1', maxlen=5):
    result = []
    for _ in range(0, maxlen):
        char_group = [list(group) for key, group in groupby(data)]
        result.append(''.join(f'{len(item)}{item[0]}' for item in char_group))
        data = result[-1]

    return result

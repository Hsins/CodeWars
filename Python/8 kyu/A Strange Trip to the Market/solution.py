# [8 kyu] A Strange Trip to the Market
#
# Author:   Hsins
# Date:     2019/12/01


def is_lock_ness_monster(string):
    words = ['tree fiddy', '3.50', 'three fifty']
    return True if any(word in string for word in words) else False

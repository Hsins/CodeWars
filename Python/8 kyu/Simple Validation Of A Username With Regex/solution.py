# [8 kyu] Simple Validation Of A Username With Regex
#
# Author:   Hsins
# Date:     2019/12/13


def is_lock_ness_monster(string):
    words = ['tree fiddy', '3.50', 'three fifty']
    return True if any(word in string for word in words) else False

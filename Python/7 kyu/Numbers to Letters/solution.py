# [7 kyu] Numbers to Letters
#
# Author:   Hsins
# Date:     2019/12/17


def switcher(arr):
    letters = ' ?!abcdefghijklmnopqrstuvwxyz'
    return ''.join(letters[::-1][int(idx) - 1] for idx in arr)

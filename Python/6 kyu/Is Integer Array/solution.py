# [6 kyu] Is Integer Array
#
# Author:   Hsins
# Date:     2020/01/03


def is_int_array(arr):
    return isinstance(arr, list) and all(isinstance(x, (int, float)) and x == int(x) for x in arr)

# [8 kyu] 5 Multiple of Index
#
# Author:   Hsins
# Date:     2019/11/28


def multiple_of_index(arr):
    result = []
    for idx, num in enumerate(arr):
        if idx == 0:
            continue
        if num % idx == 0:
            result.append(num)

    return result

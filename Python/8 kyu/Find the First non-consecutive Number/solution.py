# [8 kyu] Find the First non-consecutive Number
#
# Author:   Hsins
# Date:     2019/11/29


def first_non_consecutive(arr):
    for idx, num in enumerate(arr): 
        if num - arr[idx-1] != 1 and idx: 
            return(num)
    return None

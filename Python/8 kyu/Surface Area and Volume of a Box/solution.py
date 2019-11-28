# [8 kyu] Surface Area and Volume of a Box
#
# Author:   Hsins
# Date:     2019/11/28


def get_size(w,h,d):
    return [2 * (w*h + h*d + d*w), w * h * d]

# [8 kyu] Well of Ideas
#
# Author:   Hsins
# Date:     2019/12/10


def well(x):
    count = x.count('good')

    if count == 0:
        return 'Fail!'
    elif count > 2:
        return 'I smell a series!'
    else:
        return 'Publish!'

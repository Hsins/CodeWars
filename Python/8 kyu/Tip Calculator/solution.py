# [8 kyu] Tip Calculator
#
# Author:   Hsins
# Date:     2020/01/05
from math import ceil


def calculate_tip(amount, rating):
    rating_dict = {'TERRIBLE': 0, 'POOR': 0.05,
                   'GOOD': 0.10, 'GREAT': 0.15, 'EXCELLENT': 0.20}

    try:
        return ceil(amount * rating_dict[rating.upper()])
    except KeyError:
        return "Rating not recognised"

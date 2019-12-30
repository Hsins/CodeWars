# [7 kyu] Alphabetical Addition
#
# Author:   Hsins
# Date:     2019/12/30


def add_letters(*letters):
    sum_letter = sum([ord(char) - 96 for char in letters]) % 26
    return chr(sum_letter + 96) if sum_letter else 'z'

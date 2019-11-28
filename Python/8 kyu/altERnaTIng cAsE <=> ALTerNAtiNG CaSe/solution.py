# [8 kyu] altERnaTIng cAsE <=> ALTerNAtiNG CaSe
#
# Author:   Hsins
# Date:     2019/11/28


def to_alternating_case(string):
    return ''.join(chr.upper() if chr.islower() else chr.lower() for chr in string)

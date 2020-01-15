# [5 kyu] Regex Password Validation
#
# Author:   Hsins
# Date:     2019/12/25


regex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[A-Za-z0-9]{6,}$"

"""
^               # start letter
(?=.*?[A-Z])    # at least one uppercase letter
(?=.*?[a-z])    # at least one lowercase letter
(?=.*?[0-9])    # at least one number
[A-Za-z0-9]     # only alphanumber
{6,}            # at least 6 characters
$               # end letter
"""

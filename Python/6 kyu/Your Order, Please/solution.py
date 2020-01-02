# [6 kyu] Your Order, Please
#
# Author:   Hsins
# Date:     2020/01/03


def order(sentence):
    result = ''
    words = sentence.split()

    for _ in range(1, 10):
        for word in words:
            if word.count(str(_)) == 1:
                result += f'{word} '

    return result[:-1]

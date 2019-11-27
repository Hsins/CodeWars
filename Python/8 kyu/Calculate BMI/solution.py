# [8 kyu] Calculate BMI
#
# Author:   Hsins
# Date:     2019/11/28


def bmi(weight, height):
    bmi = weight / (height**2)

    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"

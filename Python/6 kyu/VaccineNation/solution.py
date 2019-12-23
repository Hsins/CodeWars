# [6 kyu] VaccineNation
#
# Author:   Hsins
# Date:     2019/12/23


def vaccine_list(age, status, month):
    vaccins = {
        "fiveInOne":            ['8 weeks', '12 weeks', '16 weeks'],
        "pneumococcal":         ['8 weeks', '16 weeks'],
        "rotavirus":            ['8 weeks', '12 weeks'],
        "meningitisB":          ['8 weeks', '16 weeks', '12 months'],
        "hibMenC":              ['12 months'],
        "measlesMumpsRubella":  ['12 months', '40 months'],
        "preSchoolBooster":     ['40 months'],
        "offer fluVaccine":     ['september', 'october', 'november']
    }

    result = set()
    for vaccine in vaccins:
        if age in vaccins[vaccine] or month in vaccins[vaccine] or status in vaccins[vaccine]:
            result.add(vaccine)

    return sorted(result)

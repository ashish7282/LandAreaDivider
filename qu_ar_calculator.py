import math

def qu_ar_calc(ab,bc,cd,da,bd):

    """Qaudrilateral Area Calculator"""


    s1 = (ab + bd + da) / 2
    s2 = (bc + cd + bd) / 2
    ar1 = math.sqrt(s1 * (s1 - ab) * (s1 - bd) * (s1 - da))
    ar2 = math.sqrt(s2 * (s2 - bc) * (s2 - cd) * (s2 - bd))
    ar_total = ar1 + ar2
    return ar_total
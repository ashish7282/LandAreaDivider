from qu_ar_calculator import qu_ar_calc
from angle_calc import angle_calc
import math

uwidth = []
def point_on_sid(ab, bc, cd, da, bd, m, n = -1):
    """
    must take 'b' as one end of diagonal
    Please provide tle length of quadrilateral
    in a sequence( ab, bc, cd, da, ac or bd) and
    assume side ab as front
    """
    # total area calculator
    ar_total = qu_ar_calc(ab,bc,cd,da,bd)

   
    if n == -1:
        ar_part = float(input("Enter the area of piece of field: "))
        try:
            ap1 = float(input("Enter piece length value of adjusting side (otherwise it will be default):"))
        except ValueError:    
            ap1 = a = 2 * ar_part / (da + bc) # we can give it manually
    elif n >= 1 :
        ar_part = ar_total / n # land area per person
        ap1 = ab / n  # dividing front side in 'n' equal parts    

    # here I am taking 'ad' as adjacent side
    # here I am taking 'bd' as diagonal
    # angle calculator using cosine formula
   
   # angle A, Angle C, Angle D respectively
    aa, cc, dd = angle_calc(ab,bc,cd,da,bd)

    # area of triangle of part1 front side
    ar_ft = 1 / 2 * da * ap1 * math.sin(aa)

    # calculating diagonal of part1
    dp1 = math.sqrt(da ** 2 + ap1 ** 2 - 2 * da * ap1 * math.cos(aa))  # dp1 pahle area ka diagonal hai

    # angle 'p1da' calculate karenge
    d10 = math.asin(ap1 * math.sin(aa) / dp1)
    d20 = dd - d10
    dq1 = 2 * (ar_part - ar_ft) / (dp1 * math.sin(d20))

    # calculating 'P1Q1'
    q1p1 = math.sqrt(dq1 ** 2 + dp1 ** 2 - 2 * dq1 * dp1 * math.cos(d20))

    # calculating 'q1b' and 'cq1'
    cq1 = cd - dq1
    bq1 = math.sqrt(cq1 * cq1 + bc * bc - 2 * cq1 * bc * math.cos(cc))

    # calculating 'p1b'
    p1b = ab - ap1

    # for testing
    # afp = 0.5 * dp1 * (dq1 * math.sin(d20) + da * math.sin(d10))

    # adding to 'uwidth'
    dq1 = round(dq1, 4)
    ap1 = round(ap1, 4)
    uwidth.append("dq{} : {}".format(m,dq1))
    m = m + 1
    # debug_dict = {'area_by_app': ar_part,"area_by_division": ar_part,"Total_area": ar_total}
    

    if n == -1:
        uwidth.append('ap : {}'.format(ap1))
        return uwidth
    elif n == 1:
        uwidth.append('ap : {}'.format(ap1))
        return uwidth
    else:
        return point_on_sid(p1b, bc, cq1, q1p1, bq1, m, n - 1)
    
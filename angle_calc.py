import math

def cosine_to_angle(adj1, adj2, fs):
        
        """Angle calculator Using Cosine Rule"""

        val = (adj1 ** 2 + adj2 ** 2 - fs ** 2) / (2 * adj1 * adj2)
        angle = math.acos(val)
        return angle

def angle_calc(ab,bc,cd,da,bd):
        
        """Quadrilateral Angle Calculator"""

        aa = cosine_to_angle(ab, da, bd)
        cc = cosine_to_angle(bc, cd, bd)
        dd = math.acos((bd * bd + da * da - ab * ab) / (2 * bd * da)) + math.acos((cd * cd + bd * bd - bc * bc) / (2 * cd * bd))
        return aa, cc, dd
from solver.isentropic import mach_from_area, T_ratio, P_ratio
import numpy as np

def p_abs_Pa(psig, ambient_psia = 12.9):
    P_abs = (psig + ambient_psia) * 6894.76
    return P_abs

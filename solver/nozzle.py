from solver.isentropic import mach_from_area, T_ratio, P_ratio
import numpy as np



def p_abs_Pa(psig, ambient_psia = 12.9):
    P_abs = (psig + ambient_psia) * 6894.76
    return P_abs
# area input in mm output in m^2
def circle_area_m2(diameter_mm):
    area = (np.pi * ((diameter_mm) / 1000) ** 2) / 4
    return area

def m_dot(p0, A_t, T0, gamma = 1.4, R = 296.8):
    mfr = ((p0 * A_t)/np.sqrt(T0)) * np.sqrt(gamma / R) * (2 / (gamma + 1)) ** ((gamma + 1) / (2 * (gamma - 1)))
    return mfr
print(m_dot(p_abs_Pa(80), circle_area_m2(3), 293))



if __name__ == "__main__":

    p0 = p_abs_Pa(80)
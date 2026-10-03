from solver.isentropic import mach_from_area, T_ratio, P_ratio
import numpy as np
gamma = 1.4


def p_abs_Pa(psig, ambient_psia = 12.9):
    P_abs = (psig + ambient_psia) * 6894.76
    return P_abs
# area input in mm output in m^2
def circle_area_m2(diameter_mm):
    area = (np.pi * ((diameter_mm) / 1000) ** 2) / 4
    return area

if gamma <=1:
    raise ValueError("Gamma must be greater than 1")

def m_dot(p0, A_t, T0, gamma = 1.4, R = 296.8, Cd = 1.0):
    mfr = ((p0 * A_t)/np.sqrt(T0)) * np.sqrt(gamma / R) * (2 / (gamma + 1)) ** ((gamma + 1) / (2 * (gamma - 1)))
    return mfr * Cd



def exit_conditions(p0, T0, ER, gamma = gamma, R = 296.8):
    M_exit = mach_from_area(ER, True, gamma)
    P_exit = p0 * P_ratio(M_exit, gamma)
    T_exit = T0 * T_ratio(M_exit, gamma)
    v_exit = M_exit * np.sqrt(gamma * R * T_exit)
    return {"M_exit": M_exit, "P_exit": P_exit, "T_exit": T_exit, "v_exit": v_exit}


if __name__ == "__main__":

    p0 = p_abs_Pa(80)
    result = exit_conditions(p_abs_Pa(80), 293, 1.6)
    for name, value in result.items():
        print(f"{name}: {value:.4g}")
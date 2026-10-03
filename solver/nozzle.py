from solver.isentropic import mach_from_area, T_ratio, P_ratio
import numpy as np
import matplotlib.pyplot as plt
gamma = 1.4
G0 = 9.80665

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

def divergence_loss(alpha_deg):
    np.radians(alpha_deg)
    lam = (1 + np.cos(np.radians(alpha_deg))) / 2
    return lam


def thrust_performance(p0, T0, d_throat_mm, ER, alpha_deg = 15, P_a = p_abs_Pa(0), gamma = 1.4, R = 296.8, Cd = 1.0):
    A_t = circle_area_m2(d_throat_mm)
    mfr = m_dot(p0, A_t, T0, gamma = gamma, R = R, Cd = Cd)
    A_e = ER * A_t 
    exit_state = exit_conditions(p0, T0, ER, gamma = gamma, R = R)
    F = (divergence_loss(alpha_deg) * mfr * exit_state["v_exit"]) + (exit_state["P_exit"] - P_a) * A_e
    Isp = F / (mfr * G0)
    Cf = F / (p0 * A_t)
    return {"F": F, "Isp": Isp, "Cf": Cf}

if __name__ == "__main__":

    nozzles = [("A", 1.6), ("B", 3.5)]
   
    psig = np.linspace(10, 100, 46, endpoint=True)
    F_data = {}
    Isp_data = {}
    
    for name, ER in nozzles:
        F_list = []
        Isp_list = []
        for p in psig:
            p0 = p_abs_Pa(p)
            perf = thrust_performance(p0, 293, 3, ER, alpha_deg = 15)
            F_list.append(perf["F"])
            Isp_list.append(perf["Isp"])
        F_data[name] = F_list
        Isp_data[name] = Isp_list
    
    p0 = p_abs_Pa(80)
    result = exit_conditions(p_abs_Pa(80), 293, 1.6)
    for name, value in result.items():
        print(f"{name}: {value:.4g}")
    perf = thrust_performance(p_abs_Pa(80), 293, 3, 1.6, alpha_deg = 15)
    for name, value in perf.items():
        print(f"{name}: {value:.4g}")

    plt.figure()
    plt.plot(psig, F_data["A"], label = "Nozzle A, ER = 1.6")
    plt.legend()
    plt.xlabel("Supply Pressure (psig)")
    plt.ylabel("Thrust (N)")
    plt.title("Thrust vs. Pressure")
    plt.grid(True)
    plt.plot(psig, F_data["B"], label = "Nozzle B, ER = 3.5")
    plt.legend()
    plt.axvline(26, linestyle="--", color = "black", label = "B valid above this (approx.)")
    plt.axvspan(10, 26, color = "gray")
    plt.savefig("plots/thrust_sweep.png")

    plt.figure()
    plt.plot(psig, Isp_data["A"], label = "Nozzle A, ER = 1.6")
    plt.legend()
    plt.xlabel("Supply Pressure (psig)")
    plt.ylabel("Specific Impulse (s)")
    plt.title("Specific Impulse vs. Pressure")
    plt.grid(True)
    plt.plot(psig, Isp_data["B"], label = "Nozzle B, ER = 3.5")
    plt.legend()
    plt.axvspan(10, 24, alpha=0.15, color="gray", label="model unreliable")
    plt.legend()
    plt.text(60, -15, "Nozzle B: model invalid\n(flow separates, Step 3)", fontsize=9)
    plt.savefig("plots/Isp_sweep.png")
    plt.show()
    
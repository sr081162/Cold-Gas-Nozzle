import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

M = np.linspace(0.1, 4, num=40, endpoint=True)
# T/T0 for isentropic flow, M=mach number, gamma = specific heat ratio
def T_ratio(M, gamma = 1.4):
    Tratio = ((1 + ((gamma - 1) / 2) * M**2)**-1)
    return Tratio
Tresult = T_ratio(M)
# p/p0 for isentropic flow M = mach number, gamma = specific heat ratio
def P_ratio(M, gamma = 1.4):
    Pratio = ((1 + ((gamma - 1) / 2) * M**2)**(-gamma / (gamma-1)))
    return Pratio
result = P_ratio(M)


plt.title("Isentropic Property Ratios vs. Mach Number.")
plt.plot(M, Tresult, label="T/T0")
plt.xlabel("Mach Number")
plt.ylabel("Ratio to Stagnation Value")
plt.grid(True)
plt.plot(M, result, label="p/p0")
plt.legend()
plt.savefig("plots/ratios.png")


M_area = np.linspace(0.2, 4, 40, endpoint=True)

def area_ratio(M_area, gamma = 1.4):
    Aratio =(1/M_area) * ((2/(gamma + 1)) * (1 + ((gamma - 1) / 2) * M_area**2)) ** ((gamma+1)/(2 * (gamma-1)))
    return Aratio
Aresult = area_ratio(M_area)


plt.figure()
plt.title("Area Ratio")
plt.plot(M_area, Aresult)
plt.xlabel("Mach Number")
plt.ylabel("Area Ratio")
plt.grid(True)
plt.ylim(0, 6)
plt.axvline(1, linestyle="--")
plt.savefig("plots/area_ratio.png")
plt.show()


def mach_from_area(AR, supersonic = True, gamma=1.4):
    if AR<1:
        raise ValueError("AR must be greater than 1")
    if AR == 1:
        return(1.0)
    if supersonic: 
        low, high = 1.0001, 50
    else: low, high = 0.0001, 0.9999
    def f(M):
        return area_ratio(M, gamma) - AR
    return brentq(f, low, high)
print(mach_from_area(1.0))

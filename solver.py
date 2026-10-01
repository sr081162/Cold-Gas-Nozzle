import numpy as np
import matplotlib.pyplot as plt


M = np.linspace(0.1, 4, num=50, endpoint=True)
# T/T0 for isentropic flow, M=mach number, gamma = specific heat ratio
def T_ratio(M, gamma = 1.4):
    Tratio = ((1 + ((gamma - 1) / 2) * M**2)**-1)
    return Tratio
Tresult = T_ratio(M)

def P_ratio(M, gamma = 1.4):
    Pratio = ((1 + ((gamma - 1) / 2) * M**2)**(-gamma / (gamma-1)))
    return Pratio
result = P_ratio(M)


plt.title("Isentropiuc Property Ratios vs. Mach Number.")
plt.plot(M, Tresult, label="T/T0")
plt.xlabel("Mach Number")
plt.ylabel("Ratio to Stagnation Value")
plt.grid(True)
plt.plot(M, result, label="p/p0")
plt.legend()
plt.savefig("plots/ratios.png")
plt.show()
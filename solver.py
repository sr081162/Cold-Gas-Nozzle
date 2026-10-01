# T/T0 for isentropic flow, M=mach number, gamma = specific heat ratio
def T_ratio(M, gamma = 1.4):
    ratio = ((1 + ((gamma - 1) / 2) * M**2)**-1)
    return ratio
result = T_ratio(2, 1.67)
print(result)
import pytest
from solver.isentropic import T_ratio, P_ratio, area_ratio, mach_from_area

def test_T_ratio_mach_2():
    assert T_ratio(2) == pytest.approx(0.5556, rel=1e-3)
def test_T_ratio_mach_1():
    assert T_ratio(1) == pytest.approx(0.8333, rel=1e-3)
def test_T_ratio_mach_2_g_changed():
    assert T_ratio(2, 1.67) == pytest.approx(0.4273, rel=1e-3)
def test_p_ratio_2():
    assert P_ratio(2) == pytest.approx(0.1278, rel=1e-3)
def test_A_ratio():
    assert area_ratio(2) == pytest.approx(1.6875, rel=1e-3)
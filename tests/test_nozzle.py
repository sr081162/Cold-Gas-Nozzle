import pytest
from solver.nozzle import p_abs_Pa, m_dot, circle_area_m2, exit_conditions, thrust_performance

def test_p_abs_Pa_80():
    assert p_abs_Pa(80) == pytest.approx(640500, rel=1e-3)
    
def test_p_abs_Pa_0():
    assert p_abs_Pa(0) == pytest.approx(88900, rel=1e-3)

def test_circle_area_m2_3():
    assert circle_area_m2(3) == pytest.approx(7.068583470577034e-06, rel=1e-3)

def test_m_dot():
    assert m_dot(p_abs_Pa(80), circle_area_m2(3), 293) == pytest.approx(0.010513, rel=1e-3)

def test_m_dot_double_pressure():
    assert m_dot(2 * p_abs_Pa(80), circle_area_m2(3), 293) == pytest.approx(2 * m_dot(p_abs_Pa(80), circle_area_m2(3), 293), rel=1e-3)

def test_m_dot_Cd_09():
    assert m_dot(p_abs_Pa(80), circle_area_m2(3), 293, Cd = 0.9) == pytest.approx(0.9 * m_dot(p_abs_Pa(80), circle_area_m2(3), 293), rel=1e-3)

def test_exit_conditions():
    assert exit_conditions(p_abs_Pa(80), 293, 1.6) == pytest.approx({'M_exit': 1.935, 'P_exit': 9.052e+04, 'T_exit': 167.5, 'v_exit': 510.6}, rel=1e-3)

def test_thrust_performance():
    assert thrust_performance(p_abs_Pa(80), 293, 3, 1.6, alpha_deg = 0) == pytest.approx({'F': 5.386, 'Isp': 52.24, 'Cf': 1.189}, rel=1e-3)

def test_thrust_performance_alpha_15():
    assert thrust_performance(p_abs_Pa(80), 293, 3, 1.6, alpha_deg = 15) == pytest.approx({'F': 5.294, 'Isp': 51.35, 'Cf': 1.169}, rel=1e-3)
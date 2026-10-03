import pytest
from solver.nozzle import p_abs_Pa, m_dot, circle_area_m2

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
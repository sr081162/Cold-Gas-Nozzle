import pytest
from solver.nozzle import p_abs_Pa

def test_p_abs_Pa_80():
    assert p_abs_Pa(80) == pytest.approx(640500, rel=1e-3)
    
def test_p_abs_Pa_0():
    assert p_abs_Pa(0) == pytest.approx(88900, rel=1e-3)
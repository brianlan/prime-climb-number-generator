import pytest

from src.functional import get_factors


def test_get_factors():
    assert get_factors(1) == {1:1}
    assert get_factors(12) == {2:2, 3:1}
    assert get_factors(3) == {1:1, 3:1}
    assert get_factors(21) == {3:1, 7:1}
    assert get_factors(17) == {1:1, 17:1}
    assert get_factors(100) == {2:2, 5:2}
    assert get_factors(93) == {3:1, 31:1}
    assert get_factors(47) == {1:1, 47:1}
    assert get_factors(54) == {2:1, 3:3}
    assert get_factors(27) == {3:3}

    with pytest.raises(ValueError):
        get_factors(0)
    
    with pytest.raises(ValueError):
        get_factors(-5)

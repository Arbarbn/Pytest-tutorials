import pytest

@pytest.mark.parametrize("a, b, expected_output", [
    (1, 2, 3),
    (2, 3, 5),
    (5, 7, 12),
    (-3, 3, 0)
])

def test_addition(a, b, expected_output):
    assert a+b == expected_output
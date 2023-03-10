import pytest

def test_addition():
    assert add_numbers(2, 3) == 5
    with pytest.raises(TypeError):
        add_numbers("2", 3)

def add_numbers(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        raise TypeError("x and y must be integers")

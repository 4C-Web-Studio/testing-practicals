import pytest
from calculator import add, subtract, multiply, divide

@pytest.mark.parametrize("a,b,expected", [(2, 3, 5), (-2, 2, 0), (0, 0, 0)])
def test_add(a, b, expected):
    assert add(a, b) == expected

def test_subtract():
    assert subtract(8, 3) == 5

def test_multiply():
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(7, 2) == pytest.approx(3.5)

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

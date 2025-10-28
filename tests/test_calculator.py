import pytest
from src.calculator import divide

def test_divide_normal():
    assert divide(6, 3) == 2

def test_divide_float():
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError) as exc:
        divide(1, 0)
    assert str(exc.value) == "División por cero"

def test_divide_type_error():
    with pytest.raises(TypeError):
        divide("a", 2)
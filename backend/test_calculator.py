import pytest
from calculator import *

def test_add():
    assert add(5, 3) == 8

def test_subtract():
    assert subtract(10, 2) == 8

def test_multiply():
    assert multiply(5, 2) == 10

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
    
def test_sin():
    assert sin(30) == pytest.approx(0.5)
    
def test_cos():
    assert cos(60) == pytest.approx(0.5)

def test_tan():
    assert tan(45) == pytest.approx(1.0)

def test_safe_eval_basic():
    assert safe_eval("2 + 3 * 4") == 14.0
    assert safe_eval("(10 - 2) / 2") == 4.0
    assert safe_eval("sin(30) + cos(60)") == pytest.approx(1.0)
    assert safe_eval("2 ^ 3") == 8.0

def test_safe_eval_errors():
    with pytest.raises(ValueError):
        safe_eval("5 / 0")
    with pytest.raises(ValueError):
        safe_eval("import os; os.system('echo hack')")
    with pytest.raises(ValueError):
        safe_eval("x = 5")
import pytest
from faker import Faker
from calculator.calculator import Calculator

fake = Faker()

@pytest.mark.parametrize("a, b", [(fake.random_int(min=1, max=100), fake.random_int(min=1, max=100)) for _ in range(10)])
def test_add(a, b):
    assert Calculator.add(a, b) == a + b

@pytest.mark.parametrize("a, b", [(fake.random_int(min=1, max=100), fake.random_int(min=1, max=100)) for _ in range(10)])
def test_subtract(a, b):
    assert Calculator.subtract(a, b) == a - b

@pytest.mark.parametrize("a, b", [(fake.random_int(min=1, max=20), fake.random_int(min=1, max=20)) for _ in range(10)])
def test_multiply(a, b):
    assert Calculator.multiply(a, b) == a * b

@pytest.mark.parametrize("a, b", [(fake.random_int(min=1, max=100), fake.random_int(min=1, max=10)) for _ in range(10)])
def test_divide(a, b):
    assert Calculator.divide(a, b) == a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(fake.random_int(min=1, max=100), 0)

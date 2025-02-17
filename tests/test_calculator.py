import pytest
from calculator.calculator import Calculator
from faker import Faker

fake = Faker()

# Pytest fixture to generate random test data
@pytest.fixture
def random_numbers():
    return fake.random_int(min=1, max=100), fake.random_int(min=1, max=100)

def test_addition(random_numbers):
    a, b = random_numbers
    assert Calculator.add(a, b) == a + b

def test_subtraction(random_numbers):
    a, b = random_numbers
    assert Calculator.subtract(a, b) == a - b

def test_multiplication(random_numbers):
    a, b = random_numbers
    assert Calculator.multiply(a, b) == a * b

def test_division(random_numbers):
    a, b = random_numbers
    if b == 0:
        pytest.skip("Skipping division by zero case")
    assert Calculator.divide(a, b) == a / b

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(10, 0)

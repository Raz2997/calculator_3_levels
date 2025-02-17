import pytest
from faker import Faker

fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of test records to generate")

@pytest.fixture(scope="module")
def num_records(request):
    return request.config.getoption("--num_records")

@pytest.fixture(scope="module")
def test_data(num_records):
    return [(fake.random_int(min=1, max=100), fake.random_int(min=1, max=100)) for _ in range(num_records)]

@pytest.mark.parametrize("a, b", test_data)
def test_add(a, b):
    assert Calculator.add(a, b) == a + b

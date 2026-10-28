import pytest
from app import calculate_total

def test_standard_multiplication():
    assert calculate_total(15.50, 2, 0) == 31.00

def test_discount_application():
    assert calculate_total(10.00, 3, 10) == 27.00
    assert calculate_total(50.00, 2, 50) == 50.00

def test_invalid_parameters():
    with pytest.raises(ValueError):
        calculate_total(10, 2, 105)

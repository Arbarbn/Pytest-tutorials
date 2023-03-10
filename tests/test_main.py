from main import add_numbers, subtract_numbers
import pytest

def test_addition():
    assert add_numbers(2,2) == 4

def test_subtraction():
    assert subtract_numbers(2,2) == 0

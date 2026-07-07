from src.main import *
import pytest

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 5) == 5

def test_add_float_and_integer():
    assert add(2.5, 3) == 5.5

def test_add_large_numbers():
    assert add(1_000_000, 2_000_000) == 3_000_000

def test_add_negative_and_positive():
    assert add(-2, 3) == 1

def test_add_wrong_add_postivie_numbers():
    assert add_wrong(2, 3) == 5

def test_add_wrong_add_negative_numbers():
    assert add_wrong(-2, -3) == -5

def test_add_wrong_add_zero():
    assert add_wrong(0, 5) == 5

def test_add_wrong_add_float_and_integer():
    assert add_wrong(2.5, 3) == 5.5

def test_add_wrong_add_large_numbers():
    assert add_wrong(1_000_000, 2_000_000) == 3_000_000

def test_add_wrong_add_negative_and_positive():
    assert add_wrong(-2, 3) == 1


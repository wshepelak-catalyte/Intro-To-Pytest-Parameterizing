from src.main import *
import pytest

test_cases = [
    (2, 3, 5),
    (-2, -3, -5),
    (0, 5, 5),
    (2.5, 3, 5.5),
    (1_000_000, 2_000_000, 3_000_000),
    (-2, 3, 1),
]


def test_add():
    for a, b, expected in test_cases:
        assert add(a, b) == expected


def test_add_wrong():
    for a, b, expected in test_cases:
        assert add_wrong(a, b) == expected



        

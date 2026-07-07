from src.main import *
import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (0, 5, 5),
        (2.5, 3, 5.5),
        (1_000_000, 2_000_000, 3_000_000),
        (-2, 3, 1),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (0, 5, 5),
        (2.5, 3, 5.5),
        (1_000_000, 2_000_000, 3_000_000),
        (-2, 3, 1),
    ],
)
def test_add_wrong(a, b, expected):
    assert add_wrong(a, b) == expected





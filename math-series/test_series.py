import pytest
from series import fibonacci, lucas, sum_series


@pytest.mark.parametrize("test_input, expected", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8)])
def test_fib(test_input, expected):
    actual = fibonacci(test_input)
    assert actual == expected


@pytest.mark.parametrize("test_input, expected", [(0, 2), (1, 1), (2, 3), (3, 4), (4, 7), (5, 11), (6, 18)])
def test_lucas(test_input, expected):
    actual = lucas(test_input)
    assert actual == expected


@pytest.mark.parametrize("test_input, expected", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8)])
def test_sum_series_fib(test_input, expected):
    actual = sum_series(test_input)
    assert actual == expected


@pytest.mark.parametrize("test_input, expected", [(0, 2), (1, 1), (2, 3), (3, 4), (4, 7), (5, 11), (6, 18)])
def test_sum_series_lucas(test_input, expected):
    actual = sum_series(test_input, 2)
    assert actual == expected


@pytest.mark.parametrize("test_input, expected", [(0, 10), (1, 11), (2, 21), (3, 32), (4, 53), (5, 85), (6, 138)])
def test_sum_series_custom(test_input, expected):
    actual = sum_series(test_input, 10, 11)
    assert actual == expected

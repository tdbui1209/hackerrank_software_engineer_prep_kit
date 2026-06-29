import pytest

from solution import countAffordablePairs


@pytest.mark.parametrize("prices, budget, expected", [
    ([1, 2, 3, 4, 5], 7, 8),
    ([], 100, 0),
    ([5], 5, 0)
])
def test_normal_cases(prices, budget, expected):
    assert countAffordablePairs(prices, budget) == expected

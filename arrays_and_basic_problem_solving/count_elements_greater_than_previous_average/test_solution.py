import pytest

from solution import countResponseTimeRegressions


@pytest.mark.parametrize("responseTimes, expected", [
    ([100, 200, 150, 300], 2),
    ([1, 2, 3, 4, 5], 4),
    ([5, 4, 3, 2, 1], 0),
    ([100], 0),
    ([], 0),
])
def test_normal_cases(responseTimes, expected):
    assert countResponseTimeRegressions(responseTimes) == expected

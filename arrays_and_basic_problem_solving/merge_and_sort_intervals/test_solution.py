import pytest

from solution import mergeHighDefinitionIntervals


@pytest.mark.parametrize("intervals, expected", [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[100, 200]], [[100, 200]]),
    ([], []),
])
def test_normal_cases(intervals, expected):
    assert mergeHighDefinitionIntervals(intervals) == expected

import pytest

from solution import countSubarraysWithSumAndMaxAtMost


@pytest.mark.parametrize("nums, k, M, expected", [
    ([2, -1, 2, 1, -2, 3], 3, 2, 2),
    ([], 0, 0, 0),
    ([5], 5, 5, 1)
])
def test_normal_cases(nums, k, M, expected):
    assert countSubarraysWithSumAndMaxAtMost(nums, k, M) == expected

import pytest

from solution import binarySearch


@pytest.mark.parametrize("nums, target, expected", [
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 3, 4, 5], 6, -1),
    ([], 5, -1),
    ([10], 10, 0),
    ([10], 10, 0),
    ([10, 20], 20, 1)
])
def test_normal_cases(nums, target, expected):
    assert binarySearch(nums, target) == expected

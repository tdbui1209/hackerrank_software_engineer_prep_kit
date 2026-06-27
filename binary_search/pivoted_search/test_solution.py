import pytest

from solution import searchRotatedTimestamps


@pytest.mark.parametrize("nums, target, expected", [
    ([1609466400, 1609470000, 1609473600, 1609459200, 1609462800], 1609459200, 3),
    ([1609466400, 1609470000, 1609473600, 1609459200, 1609462800], 2709459200, -1),
    ([], 5, -1),
    ([10], 10, 0),
    ([10], 10, 0),
    ([10, 20], 20, 1),
    ([20, 10], 20, 0),
    ([4, 5, 6, 7, 0, 1, 2], 2, 6)
])
def test_normal_cases(nums, target, expected):
    assert searchRotatedTimestamps(nums, target) == expected

import pytest

from solution import findSmallestSubstringWindow


@pytest.mark.parametrize("patterns, S, expected", [
    (["abc", "zyx"], "xyzabcabczyx", [6, 11]),
    (["a"], "a", [0, 0]),
    (["b"], "a", [-1, -1])
])
def test_normal_cases(patterns, S, expected):
    assert findSmallestSubstringWindow(patterns, S) == expected

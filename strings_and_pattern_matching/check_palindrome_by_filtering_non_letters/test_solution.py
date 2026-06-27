import pytest

from solution import isAlphabeticPalindrome


@pytest.mark.parametrize("code, expected", [
    ("A1b2B!a", 1),
    ("Z", 1),
    ("abc123cba", 1),
    ("", 1),
    ("abc", 0),
])
def test_normal_cases(code, expected):
    assert isAlphabeticPalindrome(code) == expected

import pytest

from solution import maxDistinctSubstringLengthInSessions


@pytest.mark.parametrize("sessionsString, expected", [
    ("abcabcbb", 3),
    ("*", 0),
    ("aa", 1)
])
def test_normal_cases(sessionsString, expected):
    assert maxDistinctSubstringLengthInSessions(sessionsString) == expected

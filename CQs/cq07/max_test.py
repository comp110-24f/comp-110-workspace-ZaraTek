"""Tests find_max.py"""

__author__ = "730772738"

from find_max import find_and_remove_max


def test_find_and_remove_max_return() -> None:
    """Tests if find_and_remove_max returns the max value"""
    assert find_and_remove_max([1, 2, 3]) == 3


def test_find_and_remove_max_mutate() -> None:
    """Tests if find_and_remove_max removes all instances of max"""
    a: list[int] = [1, 2, 3, 8, 3]
    find_and_remove_max(a)
    assert a == [1, 2, 3, 3]


def test_find_and_remove_max_unconventional() -> None:
    """Tests if find_and_remove_max returns -1 for empty input"""
    assert find_and_remove_max([]) == -1

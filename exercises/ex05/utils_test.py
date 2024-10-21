"""Unit testing for utils.py"""

__author__ = "730772738"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_1() -> None:
    """Tests only_evens returns a list with only even elements in input list"""
    assert only_evens(input=[1, 2, 3]) == [2]


def test_only_evens_2() -> None:
    """Tests only_evens returns an empty list if only odd elements are in input list"""
    assert only_evens(input=[1, 5, 3]) == []


def test_only_evens_3() -> None:
    """Tests only_evens returns an empty list if an empty list is inputted"""
    assert only_evens(input=[]) == []


def test_sub_1() -> None:
    """Tests sub returns only elements between start and end indexes"""
    assert sub(input=[10, 20, 30, 40], start=1, end=3) == [20, 30]


def test_sub_2() -> None:
    """Tests sub returns empty list if start and end are the same value"""
    assert sub(input=[10, 20, 30, 40], start=1, end=1) == []


def test_sub_3() -> None:
    """Tests sub returns an entire list if start and end values are out of range"""
    assert sub(input=[10, 20, 30, 40], start=-1, end=6) == [10, 20, 30, 40]


def test_add_at_index_1() -> None:
    """Tests add_at_index correctly inserts element to into list at index"""
    test_list: list[int] = [1, 2, 3, 5]
    add_at_index(input=test_list, add_int=4, idx=3)
    assert test_list == [1, 2, 3, 4, 5]


def test_add_at_index_2() -> None:
    """Tests add_at_index adds element to the end if idx is equal to the length of the list"""
    test_list: list[int] = [1]
    add_at_index(input=test_list, add_int=2, idx=1)
    assert test_list == [1, 2]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    test_list: list[int] = []  # object to pass to add_at_index function
    with pytest.raises(IndexError):
        add_at_index(input=test_list, add_int=1, idx=1)
        # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num>
        # that is greater than the length of our <list_object>
        assert test_list == []

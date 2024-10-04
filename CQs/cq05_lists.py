"""Mutating Functions"""

__author__ = "730772838"


def manual_append(list: list[int], num: int) -> None:
    """Appends a number to a list"""
    list.append(num)


def double(list: list[int]) -> None:
    """Doubles every value in a list"""
    idx = 0
    while idx < len(list):
        list[idx] *= 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)

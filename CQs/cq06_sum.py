"""Summing the elements of a list using different loops"""

__author__ = "730772738"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of elements in a list of floats"""
    sum: float = 0.0
    idx: int = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Returns the sum of elements in a list of floats"""
    sum: float = 0.0
    for val in vals:
        sum += val
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of elements in a list of floats"""
    sum: float = 0.0
    for i in range(0, len(vals)):
        sum += vals[i]
    return float(sum)


print(w_sum([1.1, 0.9, 1.0]))
print(f_sum([1.1, 0.9, 1.0]))
print(f_range_sum([1.1, 0.9, 1.0]))

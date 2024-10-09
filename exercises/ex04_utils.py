""""""

__author__ = "730772738"


def all(list: list[int], num: int) -> bool:
    """Returns true if all numbers in list are equal to target number"""
    same_count: int = 0
    for n in list:
        if n == num:
            same_count += 1
    if same_count == len(list):
        return True
    return False


def max(input: list[int]) -> int:
    """Returns max number in a list of integers"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max: int = input[0]
    for n in input:
        if n > max:
            max = n
    return max


print(all([1, 1, 2], 1))
print(max([1, 3, 2]))

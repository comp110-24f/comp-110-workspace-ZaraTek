""""""

__author__ = "730772738"


def all(list: list[int], num: int) -> bool:
    """Returns true if all numbers in list are equal to target number"""
    if len(list) == 0:  # returns false if list is empty
        return False
    same_count: int = 0  # tracks how many are the same
    for n in list:
        if n == num:
            same_count += 1
    if same_count == len(list):  # checks if all values are the same
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


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns true if lists are equal to each other"""
    if len(list1) != len(list2):
        return False
    same_count: int = 0  # tracks how many are the same
    for n in range(len(list1)):
        if list1[n] == list2[n]:
            same_count += 1
    if same_count == len(list1):  # checks if all values are the same
        return True
    return False


def extend(list1: list[int], list2: list[int]) -> None:
    """Mutates list1 by adding values in list2"""
    for n in list2:
        list1.append(n)


print(all([1, 1, 2], 1))
print(max([1, 3, 2]))
print(is_equal([1, 0, 1], [1, 0, 1, 1]))

list1 = [1]
extend(list1, [2, 3])
print(list1)

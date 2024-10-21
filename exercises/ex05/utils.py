"""Functions to modify and create new lists"""

__author__ = "730772738"


def only_evens(input: list[int]) -> list[int]:
    """Return a new list with only even values of input list"""
    even_list: list[int] = []
    for n in input:
        if n % 2 == 0:
            even_list.append(n)
    return even_list


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Return a new list from only the input list values within range of start and end"""
    sub_list: list[int] = []
    if start < 0:
        start = 0
    if end >= len(input):
        end = len(input)
    for i in range(start, end):
        sub_list.append(input[i])
    return sub_list


def add_at_index(input: list[int], add_int: int, idx: int) -> None:
    """Add inputted integer to list at specified index"""
    if idx > len(input) or idx < 0:
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)  # extend the list by one element
    # create space for new element by shifting elements to the right
    # starts at the end - len(input), and ends at the index of the new element
    # iterates backwards to avoid overwriting values, specified by -1 step value
    for i in range(len(input) - 1, idx, -1):
        input[i] = input[i - 1]
    input[idx] = add_int


list_ = [1]
add_at_index(list_, 2, 1)
print(list_)

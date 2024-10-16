"""Find, return, and remove the largest numnber in the list"""

__author__ = "730772738"


def find_and_remove_max(input: list[int]) -> int:
    """Find, return, and remove the largest numnber in the list"""
    if len(input) == 0:
        return -1
    max: int = input[0]
    for n in input:
        if n > max:
            max = n
    i = 0
    while i < len(input):
        if input[i] == max:
            input.pop(i)
        else:
            i += 1
    return max

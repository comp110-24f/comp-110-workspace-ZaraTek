"""Exploring linked list utils in class"""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Magic method to print Node"""
        rest: str = ""
        if self.next is None:  # Base case
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def to_str(head: Node | None) -> str:
    """Way of printing Node"""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"
    

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Cannot call factorial with negative values")
    if n <= 1:
        return 1
    return n * factorial(n-1)


two: Node = Node(2, None)
one: Node = Node(1, two)
# print(two)

print(factorial(1))

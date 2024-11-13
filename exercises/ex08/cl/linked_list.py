"""Exploring linked list utils in class."""

from __future__ import annotations


class Node:
    """Node class."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializer for Node class."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Magic method to print Node."""
        rest: str = ""
        if self.next is None:  # Base case
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def last(head: Node) -> int:
    """Return last Node in linked list."""
    if head.next is None:  # Base case
        return head.value  # Node is last
    else:
        return last(head.next)


def to_str(head: Node | None) -> str:
    """Way of printing Node."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Return value of Node in linked list at given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    else:
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return maximum data value in linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    else:
        max_in_rest = max(head.next)
        if head.value > max_in_rest:
            return head.value
        else:
            return max_in_rest


# def linkify(input_list: list[int]) -> Node | None:
#     """Return a linked list given a list[int]."""
#     if not input_list:
#         return None
#     head: Node = Node(list[0])


three: Node = Node(3, None)
two: Node = Node(2, three)
one: Node = Node(1, two)
# print(two)
# print(last(one))
print(value_at(one, 2))
print(value_at(Node(10, Node(20, Node(30, None))), 0))
print(max(Node(10, Node(20, Node(30, None)))))

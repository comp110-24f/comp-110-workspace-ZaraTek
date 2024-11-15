"""Exploring linked list utils in class."""

from __future__ import annotations

__author__ = "730772738"


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


def recursive_range(start: int, end: int) -> Node | None:
    """Creates linked list w/ values from start to end."""
    if start > end:  # Edge case
        raise ValueError("Start cannot be greater then end.")
    if start == end:  # Base case
        return None
    return Node(start, recursive_range(start + 1, end))  # Recursive case


def linkify(input_list: list[int]) -> Node | None:
    """Return a linked list given a list[int]."""
    if not input_list:
        return None
    return Node(input_list[0], linkify(input_list[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a linked list where each node is multiplied by a scale factor of given list."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))


three: Node = Node(3, None)
two: Node = Node(2, three)
one: Node = Node(1, two)
# print(two)
# print(last(one))
print(value_at(one, 2))
print(value_at(Node(10, Node(20, Node(30, None))), 0))
print(max(Node(10, Node(20, Node(30, None)))))
print(linkify([10, 20, 30, 40]))

head_node = linkify([1, 2, 3])
print(scale(head_node, 2))
print(head_node)
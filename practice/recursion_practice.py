"""Practice with recursion with problems from geeksforgeeks.org."""

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


def count_nodes(head: Node | None) -> int:
    """Return number of nodes in a linked list."""
    if head is None:
        return 0
    else:
        return 1 + count_nodes(head.next)


def find_sum(head: Node | None) -> int:
    """Return sum of nodes in a linked list"""
    if head is None:
        return 0
    else:
        return head.value + find_sum(head.next)


def reverse_linked_list(head: Node | None) -> Node | None:
    if head is None or head.next is None:
        return head
    new_head = reverse_linked_list(head.next)

    head.next.next = head
    head.next = None
    return new_head


def recursive_range(start: int, end: int) -> Node | None:
    """Creates linked list w/ values from start to end."""
    if start == end:  # Base case
        return None
    return Node(start, recursive_range(start + 1, end))


three: Node = Node(3, None)
two: Node = Node(2, three)
one: Node = Node(1, two)

print(count_nodes(one))
print(find_sum(one))
print(reverse_linked_list(one))
print(recursive_range(110, 113))

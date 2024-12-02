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


def factorial(num: int) -> int:
    if num < 0:
        raise ValueError
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


def sum_of_natural_numbers(num: int) -> int:
    if num < 0:
        raise ValueError
    if num == 0:
        return 0
    return num + sum_of_natural_numbers(num - 1)


def sum_of_digits(num: int) -> int:
    num_str = str(num)
    return (
        int(num_str[0]) + sum_of_digits(int(num_str[1:]))
        if len(num_str) > 1
        else int(num_str)
    )


def power(num: int, pow: int) -> int:
    if pow == 0:
        return 1
    return num * power(num, pow - 1)


def gcd(num1: int, num2: int) -> int:
    """holy shit maybe i am the goat."""
    if num1 >= num2:
        big = num1
        small = num2
    else:
        big = num2
        small = num1
    remainder = big % small
    if remainder == 0:
        return small
    return gcd(small, remainder)


def reverse_str(s: str) -> str:
    return reverse_helper(s, len(s) - 1)


def reverse_helper(s: str, idx: int) -> str:
    if idx < 0:
        return ""
    return s[idx] + reverse_helper(s, idx - 1)


def reverse(s):
    if len(s) == 1:
        return s
    return reverse(s[1:]) + s[0]


def factorial_no_recursion(num: int) -> int:
    stack: list[int] = [num]
    idx = num
    while idx > 1:
        idx -= 1
        stack.append(idx)
    while stack:
        idx *= stack.pop()
    return idx


# print(factorial_no_recursion(3))
# print(reverse("hello"))


def fibonacci(num: int) -> int:
    if num <= 0:  # base case 1
        return 0
    if num == 1:  # base case 2
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


def fib_iter(num: int):
    stack: list[int] = [num, 0]
    res_stack = []
    while stack:
        print(stack)
        idx = stack.pop()
        if idx <= 0:
            continue
        if idx == 1:
            next = stack.pop()
            stack.append(next - 1)
            stack.append(next - 2)

        stack.append(idx - 1)
        stack.append(idx - 2)


print(fib_iter(7))
print(fibonacci(7))
# print(reverse_str("a"))
# print(gcd(56, 98))
# print(power(3, 4))
# print(sum_of_digits(9786))
# print(sum_of_natural_numbers(5))
# print("factorial", factorial(999))

three: Node = Node(3, None)
two: Node = Node(2, three)
one: Node = Node(1, two)

# print(count_nodes(one))
# print(find_sum(one))
# print(reverse_linked_list(one))
# print(recursive_range(110, 113))

"""Testing different functions"""


def get_first(input: list[str]) -> str:
    """Returns the first element in the list"""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Pop first element off of the list"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Returns first element and pops it off"""
    first: str = input[0]
    input.pop(0)
    return first


list = ["a", "b", "c"]
print(get_first(list))
remove_first(list)
print(list)
print(get_and_remove_first(list))
print(list)

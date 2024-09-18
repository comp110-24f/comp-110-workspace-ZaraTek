"""While Loop Practice"""

__author__ = "730772738"


def num_instances(phrase: str, search_char: str) -> int:
    index: int = 0
    count: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count


print(num_instances(phrase="Happy Tuesday!", search_char="z"))

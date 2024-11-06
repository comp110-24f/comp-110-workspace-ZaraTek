"""File to define Fish class."""

__author__ = "730772738"


class Fish:
    """A Fish class with age."""

    age: int

    def __init__(self) -> None:
        """Initializes Fish object with age 0."""
        self.age = 0
        return None

    def one_day(self) -> None:
        """Shifts attributes of Fish by a day."""
        self.age += 1
        return None

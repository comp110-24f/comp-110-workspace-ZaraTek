"""File to define Bear class."""

__author__ = "730772738"


class Bear:
    """A Bear class with age and hunger."""

    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Initializes Bear object with age and huger_score at 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self) -> None:
        """Shifts attributes of Bear by a day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Bear eats and increases hunger_score by the amount of fish."""
        self.hunger_score += num_fish
        return None

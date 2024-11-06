"""File to define River class."""

__author__ = "730772738"

from .fish import Fish
from .bear import Bear


class River:
    """River class populated by Fish and Bears."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Removes fish and bears who are too old."""
        surviving_fish = [fish for fish in self.fish if fish.age <= 3]
        self.fish = surviving_fish

        surviving_bears = [bear for bear in self.bears if bear.age <= 5]
        self.bears = surviving_bears

        return None

    def bears_eating(self) -> None:
        """Feed a bear and remove fish from the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self) -> None:
        """Remove a bear it is too hungry and starves."""
        surviving_bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        self.bears = surviving_bears
        return None

    def repopulate_fish(self) -> None:
        """Fish reproduce 4 for every 2 in the river."""
        new_fish_count: int = (len(self.fish) // 2) * 4
        for _ in range(new_fish_count):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self) -> None:
        """Bear reproduce 1 for every 2 in the river."""
        new_bears_count: int = len(self.bears) // 2
        for _ in range(new_bears_count):
            self.bears.append(Bear())
        return None

    def view_river(self) -> None:
        """Print the river status."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def remove_fish(self, amount: int) -> None:
        """Remove fish from the river."""
        for _ in range(amount):
            if self.fish:
                self.fish.pop(0)
        return None

    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        return None

    def one_river_week(self) -> None:
        """Makes a week go by."""
        for _ in range(7):
            self.one_river_day()
        return None

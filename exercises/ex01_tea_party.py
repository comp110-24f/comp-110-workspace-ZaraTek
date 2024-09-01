"""A program to help plan a tea party by calculating what is needed and the expected cost"""

__author__: str = "730772738"


def main_planner(guests: int) -> None:
    """Calls each function and produces output"""
    print(
        "A Cozy Tea Party for ", guests, " People", sep=""
    )  # used sep="" to get rid of the extra space
    print("Tea Bags: ", tea_bags(guests), sep="")
    print("Treats: ", treats(guests), sep="")
    print("Cost: $", cost(tea_bags(guests), treats(guests)), sep="")


def tea_bags(people: int) -> int:
    """Computes # of tea bags needed based on # of guests"""
    return people * 2


def treats(people: int) -> int:
    """Computes # of treats needed based on # of guests"""
    return int(
        tea_bags(people=people) * 1.5
    )  # must typecast to int to avoid error since multiplying by float


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of tea bags and treats combined"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

"""Testing functions in list_fns.py"""

from list_fns import get_first, remove_first


def test_get_first() -> None:
    assert get_first(input=["Viktorya", "Samy", "Izzi"]) == "Viktorya"


def test_remove_first() -> None:
    my_TAs: list[str] = ["Viktorya", "Samy", "Benjamin"]
    remove_first(my_TAs)
    assert my_TAs == ["Samy", "Benjamin"]

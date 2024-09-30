__author__ = "730772738"


def get_coords(xs: str, ys: str) -> None:
    """Prints strings in coordinate form"""
    i: int = 0
    while i < len(xs):
        j: int = 0
        while j < len(ys):
            print("(" + xs[i] + ",", ys[j] + ")", sep="")
            j += 1
        i += 1


if __name__ == "__main__":
    get_coords("12", "34")
    get_coords("hi", "bye")

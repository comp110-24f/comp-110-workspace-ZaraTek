def celsius_to_fahrenheit(degrees_c: int) -> float:
    """Convert degrees Celsius to degrees Fahrenheit"""
    return (degrees_c * 9 / 5) + 32


boiling_point = celsius_to_fahrenheit(100)
print(boiling_point)


def division(x: int, y: int) -> float:
    return y / x
    print(y % x)


print(division(y=64, x=16))

print(int(64 / 16))

x: int = 1
x = x + 1
print("x:", x)

xs = "01"
ys = "23"


def get_coords() -> None:
    x_idx: int = 0
    while x_idx < len(xs):
        y_idx: int = 0
        while y_idx < len(ys):
            print(f"({xs[x_idx]},{ys[y_idx]})")
            y_idx += 1
        x_idx += 1


get_coords()

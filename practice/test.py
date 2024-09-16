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

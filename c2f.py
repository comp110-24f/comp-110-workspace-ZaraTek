def celsius_to_fahrenheit(degrees_c: int) -> float:
    """Convert degrees Celsius to degrees Fahrenheit"""
    return (degrees_c * 9 / 5) + 32


boiling_point = celsius_to_fahrenheit(100)
print(boiling_point)

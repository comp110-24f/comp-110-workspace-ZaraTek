points: dict[str, int] = {"Kris": 0, "Kaki": 10}
points["Kaki"] += 100

for name in points:
    point = points[name]
    print(name, point)


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print(dict1)

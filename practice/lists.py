print(list[str])
print([])
names = ["Kris", "Kaki", "Alyssa"]
print(names[0])
print(list())
print(len(names))

names.append("Zara")
print(names)
names[3] = "Chloe"
print(names)

"""
a: str = "24"
b: str = a
a += "6"
print(b)
"""

a: list[int] = [2, 4]
b: list[int] = a
b.append(6)
print(a)

x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0
print(y)

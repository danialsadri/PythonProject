from math import hypot


class Point:
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def distance(self, other: "Point") -> float:
        return hypot(self.x - other.x, self.y - other.y)


p1 = Point()
p2 = Point()

# <object>.<attribute> = <value>
p1.x = 5
p1.y = 3

p2.x = 10
p2.y = 15

print(f"p1 = x: {p1.x} y: {p1.y}")
print(f"p2 = x: {p2.x} y: {p2.y}")
# p1.reset()
# Point.reset(p1)
# p2.reset()
# Point.reset(p2)
print(f"p1 = x: {p1.x} y: {p1.y}")
print(f"p2 = x: {p2.x} y: {p2.y}")
print(f"distance= {p1.distance(p2)}")

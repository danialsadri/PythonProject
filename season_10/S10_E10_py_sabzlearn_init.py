from math import hypot


class Point:
    # method
    # attribute default / non default
    def __init__(self, x: float = 0, y: float = 0):
        # self.x = x
        # self.y = y
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def distance(self, other: "Point") -> float:
        return hypot(self.x - other.x, self.y - other.y)


p1 = Point()
p2 = Point()

# p1.x = 10
# p1.y = 15
#
# p2.x = 12
# p2.y = 16

print(f"p1 = x: {p1.x} y: {p1.y}")
print(f"p2 = x: {p2.x} y: {p2.y}")
# p2.reset()
# Point.reset(p2)
# p2.move(100, 200)
# print(f"distance= {p1.distance(p2)}")
# print(f"p1 = x: {p1.x} y: {p1.y}")
# print(f"p2 = x: {p2.x} y: {p2.y}")


# ----------------------------------------
"""
متد __new__  وظیفه ساخت شی رو بر عهده داره  و قبل اینکه
 اون شی ساخته شده رو ریترن کنه میاد این متد __init__ رو صدا میزنه تا مقدار دهی اولیه انجام بده مثل متد ها و اتریبیوت ها
"""
# __new__ -> create -> ساخت شی
# __init__ -> initialize -> مقدار دهی اولیه

p3 = Point(5, 55)
print(f"p3 = x: {p3.x} y: {p3.y}")

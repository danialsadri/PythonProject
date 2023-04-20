from math import hypot


# """
# چه چیز هایی داخل داک استریگ کلاس میویسیم؟؟؟
# توضیح کلی و مختصر و مفید در مورد هدف کلاس
# """
# """
#     A point on the axis provides two-dimensional coordinates.
#     # example
#     # methods
#     # attributes
#     # interface
# """


class Point:
    """
    A point on the axis provides two-dimensional coordinates.
    >>> p1 = Point()
    >>> p2 = Point(3, 4)
    >>> p2.reset()
    >>> p1.distance(p2)
    0.0
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Initialize the x and y coordinates of the new point.
        :param x: x-coordinates
        :param y: y-coordinates
        """
        self.x = x
        self.y = y

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def distance(self, other: "Point") -> float:
        return hypot(self.x - other.x, self.y - other.y)


p1 = Point()
p2 = Point()
p3 = Point(5, 55)

# print(f"p1 = x: {p1.x} y: {p1.y}")
# print(f"p2 = x: {p2.x} y: {p2.y}")
# print(f"p3 = x: {p3.x} y: {p3.y}")
# print(Point.__doc__)
# print(help(Point))
import doctest

doctest.testmod()

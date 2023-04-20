from math import hypot
from time import sleep
from typing import Optional

__all__ = ["_x", "y"]
_x = 10
y = 20

class Point:
    # """
    # A point on the axis provides two-dimensional coordinates.
    # >>> p1 = Point()
    # >>> p2 = Point(3, 4)
    # >>> p2.reset()
    # >>> p1.distance(p2)
    # 0.0
    # """

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


point: Optional[Point] = None


def get_point():
    global point
    if not point:
        point = Point()
        sleep(5)
    return point


def main():
    po_1 = get_point()
    po_1.move(5, 10)
    print(f"x= {po_1.x} y={po_1.y}")


if __name__ == "__main__":
    main()

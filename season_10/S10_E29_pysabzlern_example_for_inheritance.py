class Shape:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.area = 0
        self.perimeter = 0

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def show(self):
        info = ""
        for key, value in self.__dict__.items():
            if value > 0:
                info += f"{key}: {value:.2f}\n"
        print(info)

    def __str__(self):
        return self.__class__.__name__


# length, width
class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.length * self.width

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.length + self.width)


# length
class Square(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.length ** 2

    def calculate_perimeter(self):
        self.perimeter = 4 * self.length


# base, height, side1, side2
class Triangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = (self.base * self.height) / 2

    def calculate_perimeter(self):
        self.perimeter = self.base + self.side1 + self.side2


# diameter1, diameter2, length
class Rhombus(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = (self.diameter1 * self.diameter2) / 2

    def calculate_perimeter(self):
        self.perimeter = self.length * 4


# length, height, width
class Parallelogram(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.length * self.height

    def calculate_perimeter(self):
        self.perimeter = (self.length + self.width) * 2


# height, base, top, side1, side2
class Trapezium(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = 1 / 2 * self.height * (self.top + self.base)

    def calculate_perimeter(self):
        self.perimeter = self.top + self.base + self.side1 + self.side2


# radius
class Circle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.radius ** 2 * 3.14

    def calculate_perimeter(self):
        self.perimeter = 2 * self.radius * 3.14


rectangle = Rectangle(length=2, width=6)
rectangle.calculate_area()
rectangle.calculate_perimeter()
print(rectangle)
rectangle.show()
print('-' * 50)

square = Square(length=4)
square.calculate_area()
square.calculate_perimeter()
print(square)
square.show()
print('-' * 50)

triangle = Triangle(base=4, height=3, side1=3, side2=5)
triangle.calculate_area()
triangle.calculate_perimeter()
print(triangle)
triangle.show()
print('-' * 50)


rhombus = Rhombus(diameter1=6, diameter2=10, length=6)
rhombus.calculate_area()
rhombus.calculate_perimeter()
print(rhombus)
rhombus.show()
print('-' * 50)


parallelogram = Parallelogram(length=6, height=2, width=4)
parallelogram.calculate_area()
parallelogram.calculate_perimeter()
print(parallelogram)
parallelogram.show()
print('-' * 50)


Trapezium = Trapezium(height=4, base=8, top=5, side1=4, side2=5)
Trapezium.calculate_area()
Trapezium.calculate_perimeter()
print(Trapezium)
Trapezium.show()
print('-' * 50)


circle = Circle(radius=4)
circle.calculate_area()
circle.calculate_perimeter()
print(circle)
circle.show()
print('-' * 50)

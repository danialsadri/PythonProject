# ---------------------------------
# x = [1, 2, 3, 4, 5]
# print(callable(x))
# ---------------------------------
# def func(x):
#     print(x ** 2)
#
#
# func(5)
# ---------------------------------
# class A:
#     def __init__(self, x):
#         print('init')
#         self.x = x
#
#     def __call__(self, z):
#         print('call')
#         self.z = z
#
#
# obj = A(10)
# obj(2)
# print(f"x= {obj.x} z= {obj.z}")
# ---------------------------------
# class Shape:
#     def __init__(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#         self.area = 0
#         self.perimeter = 0
#
#     def calculate_area(self):
#         pass
#
#     def calculate_perimeter(self):
#         pass
#
#     def show(self):
#         info = ""
#         for key, value in self.__dict__.items():
#             if value > 0:
#                 info += f"{key}: {value:.2f}\n"
#         print(info)
#
#     def __str__(self):
#         return self.__class__.__name__
#
#
# class Square(Shape):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#     def calculate_area(self):
#         self.area = self.length ** 2
#
#     def calculate_perimeter(self):
#         self.perimeter = 4 * self.length
#
#     def __call__(self, **kwargs):
#         super().__init__(**kwargs)
#
#
# square = Square(length=4)
# square.calculate_area()
# square.calculate_perimeter()
# print(square)
# square.show()
# print('-' * 50)
#
#
# square(length=8)
# square.calculate_area()
# square.calculate_perimeter()
# print(square)
# square.show()
# print('-' * 50)
# ---------------------------------

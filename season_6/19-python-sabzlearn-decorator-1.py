# ----------------------  1  ----------------------------------
# def dec(func):
#     def inner():
#         print('*' * 20)
#         func()
#         print('*' * 20)
#
#     return inner
#
#
# def f_1():
#     print('danial')
#
#
# def f_2():
#     print('mohammad')
#
#
# new_func1 = dec(f_1)
# new_func2 = dec(f_2)
#
# new_func1()
# new_func2()
# ----------------------  2  ----------------------------------
# def dec(func):
#     def inner():
#         print('*' * 20)
#         func()
#         print('*' * 20)
#
#     return inner
#
#
# @dec
# def f_1():
#     print('danial')
#
#
# @dec
# def f_2():
#     print('mohammad')
#
#
# f_1()
# f_2()
# ----------------------  3  ----------------------------------
# def dec(func):
#     def inner(x, y):
#         if y == 0:
#             print('warning!')
#         else:
#             func(x, y)
#
#     return inner
#
#
# def f(x, y):
#     print(x / y)
#
#
# func1 = dec(f)
#
# func1(125, 9)
# ----------------------  4  ----------------------------------
# def dec(func):
#     def inner(x, y):
#         if y == 0:
#             print('warning!')
#         else:
#             func(x, y)
#
#     return inner
#
#
# @dec
# def f(x, y):
#     print(x / y)
#
#
# f(10, 5)
# ----------------------  5  ----------------------------------
# def dec(func):
#     def inner(x, y):
#         if y == 0:
#             return 'warning!'
#         return func(x, y)
#
#     return inner
#
#
# @dec
# def f(x, y):
#     return x / y
#
#
# print(f(10, 5))
# ----------------------  6  ----------------------------------
# def dec(func):
#     def inner(*x, **y):
#         if y == 0:
#             return 'warning!'
#         return func(*x, **y)
#
#     return inner
#
#
# @dec
# def f(x, y):
#     return x / y
#
#
# print(f(10, 5))

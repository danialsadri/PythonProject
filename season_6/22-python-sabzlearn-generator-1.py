# ==============================================================
# def func(x):
#     return x ** 2
#
#
# y = func(5)
# print(y)
# ==============================================================
# def func(x):
#     print("reza")
#     yield x ** 2
#     print("hello")
#     yield 5
#     print('ok')
#     yield x-2
#
#
# y = func(5)
# print(next(y))
# print(next(y))
# print(next(y))
# ==============================================================
# def my_generator():
#     for i in range(0, 1000+1):
#         yield i ** 2
#
#
# g = my_generator()
# print(next(g))
# print(next(g))
# print(next(g))
# ==============================================================
# def my_generator():
#     for i in range(0, 1000+1):
#         yield i ** 2
#
#
# g = my_generator()
# for i in g:
#     print(i)
# ==============================================================

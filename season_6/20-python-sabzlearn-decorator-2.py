# ----------------------  1  ----------------------------------
# def dec(func):
#     def inner(*x, **y):
#         if y == 0:
#             return 'warning!'
#         return func(*x, **y)
#     return inner
#
#
# @dec
# def f(x, y):
#     return x / y
#
#
# print(f(10, 5))
# ----------------------  2  ----------------------------------
# def dash(func):
#     def inner(*x, **y):
#         print('-' * 20)
#         func(*x, **y)
#         print('-' * 20)
#     return inner
#
#
# def plus(func):
#     def inner(*x, **y):
#         print('+' * 20)
#         func(*x, **y)
#         print('+' * 20)
#     return inner
#
#
# def star(func):
#     def inner(*x, **y):
#         print('*' * 20)
#         func(*x, **y)
#         print('*' * 20)
#     return inner
#
#
# @plus
# @dash
# @star
# def msg(name):
#     print(f"I am {name}")
#
#
# msg('reza')
# ----------------------  3  ----------------------------------
# def dash(function):
#     def inner(*args, **kwargs):
#         print('-' * 20)
#         function(*args, **kwargs)
#         print('-' * 20)
#     return inner
#
#
# def plus(function):
#     def inner(*args, **kwargs):
#         print('+' * 20)
#         function(*args, **kwargs)
#         print('+' * 20)
#     return inner
#
#
# def star(function):
#     def inner(*args, **kwargs):
#         print('*' * 20)
#         function(*args, **kwargs)
#         print('*' * 20)
#     return inner
#
#
# def message(name):
#     print(f'I am {name}')
#
#
# printer = plus(dash(star(message)))
#
# printer('reza')
# ----------------------  4  ----------------------------------
# def star(a):
#     def inner1(func):
#         def inner2(*x, **y):
#             print('*' * a)
#             func(*x, **y)
#             print('*' * a)
#
#         return inner2
#     return inner1
#
#
# @star(10)
# def msg(name):
#     print(f"I am {name}")
#
#
# msg('reza')
# ----------------------  5  ----------------------------------
# from functools import wraps
#
#
# def star(func):
#     @wraps(func)
#     def inner(*x, **y):
#         print('*' * 10)
#         func(*x, **y)
#         print('*' * 10)
#
#     return inner
#
#
# @star
# def msg(name):
#     """prints a message"""
#     print(f'I am {name}')
#
#
# print(msg.__doc__)
# print(msg.__name__)

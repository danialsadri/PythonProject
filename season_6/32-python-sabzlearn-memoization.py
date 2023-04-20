# from functools import wraps
#
#
# # 0 1 1 2 3 5 8 13 21 34 55
# # 0 1 2 3 4 5 6  7  8  9  10
# def memoize(func):
#     memory = {}
#
#     @wraps(func)
#     def wrapper_decorator(n):
#         if n not in memory:
#             memory[n] = func(n)
#         return memory[n]
#
#     return wrapper_decorator
#
#
# @memoize
# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(87))

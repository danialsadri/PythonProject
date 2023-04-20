# =================================== recursive decorator===============================================
# from functools import wraps
# from time import sleep
# def dec(func):
#     @wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         print('*' * 40)
#         value = func(*args, **kwargs)
#         print('-' * 40)
#         return value
#     return wrapper_decorator
# @dec
# def rev(n):
#     if n <= 0:
#         return None
#     sleep(1)
#     print(n)
#     rev(n - 1)
# rev(10)
# =================================== recursive generator ===============================================
# from time import sleep
# def g_rev(n):
#     if n <= 0:
#         return None
#     sleep(1)
#     yield n
#     for i in g_rev(n - 1):
#         yield i
#
#
# g = g_rev(10)
# print(list(g))
# ======================================================================================================
# from time import sleep
# from sys import getrecursionlimit, setrecursionlimit
#
# print(getrecursionlimit())
# print(setrecursionlimit(10000))
#
#
# def rev(n):
#     if n <= 0:
#         return None
#     # sleep(1)
#     print(n)
#     rev(n - 1)
#
#
# rev(1000)
# ======================================================================================================

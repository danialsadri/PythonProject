# ======================================================================================================================
# from functools import wraps


# def my_decorator_func(cls):
#     @wraps(cls)
#     def wrapper_func(*args, **kwargs):
#         print('*' * 20)
#         obj1 = cls(*args, **kwargs)
#         print('*' * 20)
#         return obj1
#     return wrapper_func


# ------------------------------
# @my_decorator_func
# class Test:
#     """Class Test!!!"""
#     pass


# obj = Test()
# print(obj)
# print(Test.__doc__)
# ------------------------------
# class Test:
#     pass
#
#
# NewTest = my_decorator_func(Test)
# obj = NewTest()
# print(obj)
# ------------------------------

# ======================================================================================================================
# from functools import update_wrapper
#
#
# class MyClassDecorator:
#     def __init__(self, func):
#         update_wrapper(self, func)
#         self.func = func
#
#     def __call__(self):
#         print('*' * 20)
#         obj1 = self.func()
#         print('*' * 20)
#         return obj1

# -----------------------------
# @MyClassDecorator
# def my_func():
#     """My Function"""
#     print('reza')
#
#
# my_func()
# print(my_func.__doc__)
# -----------------------------
# def my_func():
#     """My Func"""
#     print('reza')
#
#
# new_func = MyClassDecorator(my_func)
# new_func()
# print(my_func.__doc__)
# -----------------------------
# @MyClassDecorator
# class Test:
#     def __init__(self):
#         self.a = 5
#
#
# obj = Test()
# print(obj)
# print(obj.a)
# -----------------------------
# ======================================================================================================================

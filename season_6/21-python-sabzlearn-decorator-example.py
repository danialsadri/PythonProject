# ===============================  1  ================================================
# from functools import wraps
#
# passwords = {'reza': '4344', 'ali': '5422', 'hossein': '6432', 'hasan': "4325"}
# blacklist = {'ali', 'reza'}
#
#
# def ban(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         if args[0] in blacklist:
#             print('This user is blocked')
#         else:
#             func(*args, **kwargs)
#
#     return inner
#
#
# @ban
# def print_password(username):
#     print(f"{username}: {passwords[username]}")
#
#
# @ban
# def change_password(username, new_password):
#     passwords[username] = new_password
#     print(f"{username}: {passwords[username]}")
# ===============================  2  ================================================
# from time import perf_counter
# from functools import wraps
#
#
# def time_calculation(func):
#     @wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         start_time = perf_counter()
#         value = func(*args, **kwargs)
#         end_time = perf_counter()
#         run_time = end_time - start_time
#         print(f"The run time of {func.__name__} is: {run_time}")
#         return value
#
#     return wrapper_decorator
#
#
# @time_calculation
# def number(x):
#     s = 0
#     for i in range(1, x + 1):
#         s += i ** 2
#
#
# @time_calculation
# def fact(x):
#     f = 1
#     for i in range(1, x + 1):
#         f *= i
#
#
# number(100000)
# fact(100000)

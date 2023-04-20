# descending = نزولی
# ascending = صعودی
# ==========================================================
# 1. Can be created at runtime.
# 2. Can be assigned to a variable.
# 3. Can be passed as a argument to a function.
# 4. Can be return as a result from a function.
# 5. Can have properties and methods.
# ========================  1  ==================================
# def A(a):
#     print(a)
#     def B(b):
#         print(b ** 2)
#     B(a)
# A(5)
# ========================  2  ==================================
# def cube(x):
#     return x ** 3
#
#
# y = int(input('y: '))
# n = cube #  اینجا اگه پرانتز های تابع رو نزارم یعنی اینکه خود تابع رو گذاشتم داخل اون متغیر
# print(n(y))
# ========================  3  ==================================
# def ascending(mylist):
#     print(sorted(mylist))
#
#
# def descending(mylist):
#     print(sorted(mylist, reverse=True))
#
#
# def mysort(f, mylist):
#     f(mylist)
#
#
# mysort(descending, [54235, 5464, 326, 36, 34, 6, 3, 6, 32, 6, 5, 32, 64, 326, 4, 623])
# ========================  4  ==================================
# def mysort(s):
#     def ascending(x):
#         print(sorted(x))
#
#     def descending(y):
#         print(sorted(y, reverse=True))
#
#     def error(z):
#         print('Error!', z)
#
#     if s == 'a':
#         return ascending
#     elif s == 'd':
#         return descending
#     else:
#         return error
#
#
# action = input('action: ')
# func = mysort(action)
# func([4215, 421, 5, 54235, 425, 54235, 243, 5, 432, 5, 23415, 4235, 234, 5, 23, 45, 23, 45])
# ===============================================================

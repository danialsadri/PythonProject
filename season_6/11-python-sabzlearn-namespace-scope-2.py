# x = 0
# def A():
#     x = 10
#     def B():
#         x = 22
#         print(x)
#     B()
# A()
# ==================================
# x = 5
# def A():
#     x = 10
#     def B():
#         global x
#         x += 20
#         print(x)
#     B()
# A()
# print(x)
# ==================================
# x = 5
# def A():
#     x = 10
#
#     def B():
#         nonlocal x
#         x += 20
#         print(x)
#     B()
# A()
# print(x)
# ==================================
# x = 5
# def D():
#     x = 8
#     def A():
#         nonlocal x
#         def B():
#             nonlocal x
#             x += 20
#             print(x)
#         B()
#     A()
# D()
# print(x)
# ==================================

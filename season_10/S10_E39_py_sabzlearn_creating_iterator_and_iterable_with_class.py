# ======================================================================================================================
# list_ = [1, 2, 3]
# print("__iter__" in dir(list_))
# print("__next__" in dir(list_))
# for i in list_:
#     print(i)
# iter_list = iter(list_)
# print("__next__" in dir(iter_list))
# print(next(iter_list))
# -------------------------------
#  ایتریتور ها اخرین مقدار رو توی خودشون ذخیره میکنن
# iter_list = iter(list_)
# next(iter_list)
# for i in iter_list:
#     print(i)
# ======================================================================================================================
# class NewObject:
#     def __init__(self):
#         self.x = 5
#
#     def __iter__(self):
#         for i in range(5):
#             yield i
#
#     def __next__(self):
#         self.x += 2
#         return self.x


# n = NewObject()
# for i in n:
    # print(i)
# print(next(n))
# for i in n:
#     print(i)

# print('-'*30)
# print(next(n))
# print(next(n))
# print('-'*30)

# n1 = iter(n)
# for j in n1:
#     print(j)
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# ======================================================================================================================
# class PowTwo:
#     def __init__(self, max_pow):
#         self.n = 0
#         self.max_pow = max_pow
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n <= self.max_pow:
#             result = self.n ** 2
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
#
#
# n = PowTwo(max_pow=5)
# --------------------------
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# --------------------------
# for i in n:
#     print(i)
# --------------------------
# n1 = iter(n)
# next(n1)
# next(n1)
# for i in n1:
#     print(i)
# --------------------------

# from time import perf_counter
# ==================================================================
# def list_range(start, end, step=1):
#     new_range = []
#     while start < end:
#         new_range.append(start)
#         start += step
#     return new_range
# ==================================================================
# def gen_range(start, end, step=1):
#     while start < end:
#         yield start
#         start += step
# ==================================================================
# start = perf_counter()
# lr = list_range(1, 10000000)
# s = 0
# for i in lr:
#     if i == 3:
#         break
#     s += i ** 2
# end = perf_counter()
# print(f"lr: {end-start}")
# -----------------------------------------------------------------
# start2 = perf_counter()
# gr = gen_range(1, 1000000000000000000000000000000000000000000000000000000000000000000000000)
# s = 0
# for j in gr:
#     if j == 3:
#         break
#     s += j ** 2
# end2 = perf_counter()
# print(f"gn: {end2-start2}")
# =================================================================================================
# def my_generator(r=10):
#     for i in range(r):
#         yield i ** 2


# g = my_generator()
# --------------------------------------
# g.close()  # ژنراتور من رو میبنده
# --------------------------------------
# for i in g:
#     if i == 16:
#         g.throw(ValueError('Error!!!'))  # باعث رخ دادن اروری میشود
#     print(i)
# --------------------------------------
# print(list(g))
# =================================================================================================
# def square_gn(nums):
#     for i in nums:
#         yield i ** 2
#
#
# def even_gn(nums):
#     for i in nums:
#         if i % 2 == 0:
#             yield i
#
#
# sg = square_gn([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# eg = even_gn([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# print(list(sg))
# print(list(eg))
# print(sum(square_gn(even_gn([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))))
# =================================================================================================

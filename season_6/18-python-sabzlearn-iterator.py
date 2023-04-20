# Iterate ==> تکرار کردن
# Iteration ==> تکرار یا عمل تکرار ==> رفتار تکرار کردن را برای ما نشون میده : for, while
# Iterable ==> قابل تکرار یا تکرار پذیر ==> همه ابجکت هایی که بتونیم روی انها عمل تکرار کردن رو انجام بدیم یاااا همه ابجکت هایی که بتونم انها رو به ایتریتور تبدیل کنم
# Iterator ==> تکرار کننده یا تکرار گر ==> ابجکت هایی هست که اخرین وضعیت خودشون رو حفظ میکنن یااا بتونم متد نکث رو روی انها اجرا کنم

# ----------------------------
# i = [1, 2, 3, 4, 5]
# print("__next__" in dir(i))
# i = iter(i)
# print("__next__" in dir(i))
# ----------------------------
# i = [1, 2, 3, 4, 5]
# i = iter(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# ----------------------------
# i = [1, 2, 3, 4, 5]
# i = i.__iter__()
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# ----------------------------
# i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = iter(i)
# while True:
#     try:
#         print(next(i))
#     except StopIteration:
#         break
# ----------------------------
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in l:
#     print(i)
# ----------------------------
# from itertools import count
#
# counter = count()
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# ----------------------------

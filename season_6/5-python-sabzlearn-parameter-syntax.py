# normal
# default = value
# normal & default = value
# *name
# normal & default = value & *name
# **name
# normal & default = value & *name & **name
# ------------------  normal  ----------------------------------------
# def func(a, b, c):  # normal
#     print(f"a= {a} b= {b} c= {c}")
#
#
# func(1, 2, 3)
# ------------------  default = value  -------------------------------
# def func(a=5, b=3, c=1):  # default = value # اگر توی پارامتر ها مقدار پیشفرض براش بزاری دیگه لازم نیست توی ارگومان مقدار بدی
#     print(f"a= {a} b= {b} c= {c}")
#
#
# func()
# func(22, 44)
# func(b=0)
# ------------------  normal & default = value  ----------------------
# def func(a, b, c=5):  # normal & default = value # اول باید موقعیتی باشه بعدش دیفالت ولیو
#     print(f"a= {a} b= {b} c= {c}")
#
#
# func(1, 2)
# func(b=6, a=3)
# ------------------  *name  -----------------------------------------
# # اونی که با استار تعریف شده دیگه نباید به صورت نیم ولیو براش ارگومانی نوشته بشه
# def func(a, b, *c, d):  # *name
#     print(f"a= {a} b= {b} c= {c} d= {d}")
#
#
# # func(1, 2, 3, 4, 5, 6, 7, 8, 9)
# func(1, 2, 3, 4, 5, 6, 7, 8, 9, d=43)
# ------------------  normal & default = value & *name  --------------
# def func(a, b=9, *c):  # normal & default = value & *name
#     print(f"a= {a} b= {b} c= {c}")
#
#
# func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# func(22)
# ------------------  **name  -----------------------------------------
# def func(**a):  # **name
#     print(f"a= {a}")
#
#
# func(a=66, b=33, c=22, d=88)
# -----  normal & default = value & *name & **name  ------------------
# def func(a, b=0, *c, **d):
#     print(f"a= {a}\nb= {b}\nc= {c}\nd= {d}")
#
#
# func(2, 44, 33, 43214, 42, 24, 42, 64, 76, 85, c=55, d=66, e=77, f=88)
# --------------------------------------------------------------------

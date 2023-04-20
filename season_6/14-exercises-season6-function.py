# ======================================  1  =============================================
# تابعی بنویسید که کار تابع داخلی len را انجام دهد

# def len2(iterable):
#     counter = 0
#     for _ in iterable:
#         counter += 1
#     return counter
#
#
# print(len2([542, 54, 2, 5, 324, 5, 43, 5, 34, 5, 325, 34]))

# ======================================  2  =============================================
# تابعی بنویسید که کار تابع داخلی max یا  min را انجام دهد

# def max2(*args):
#     m = args[0]
#     for i in args:
#         if i > m:
#             m = i
#     return m
# print(max2(523465326, 63426365476526, 5326, 6564, 5, 6, 35))

# ======================================  3  =============================================
# تابعی بنویسید که کار تابع داخلی sum را انجام دهد

# def sum2(iterable):
#     s = 0
#     for i in iterable:
#         s += i
#     return s
#
#
# print(sum2([1, 2, 3, 4, 5]))

# ======================================  4  =============================================
# تابعی بنوسید که یک عدد به عنوان ورودی گرفته تشخیص دهد عدد مربع است یا خیر

# def square(n):
#     for i in range(1, n):
#         if i ** 2 == n:
#             print(f'Yes! {i} * {i} = {n}')
#             break
#     else:
#         print('No!')
#
#
# x = int(input('x: '))
# square(x)

# ======================================  5  =============================================
# تابعی بنویسید که قیمت کالا و درصد تخفیف را گرفته و قیمت پس از تخفیف را محاسبه کند

# def discount(price, rate):
#     discount_rate = int(price * rate / 100)
#     new_price = price - discount_rate
#     print(f"discount rate: {discount_rate}\nnew price: {new_price}")
#
#
# price = int(input('price: '))
# rate = int(input('rate: '))
#
# discount(price, rate)

# ======================================  6  =============================================
#  تابعی بنوسید که یک کاراکتر را خوانده و مشخص کند کاراکتر یک رقم , حروف بزرگ ,  حروف کوچک , سابر نماد است

# def func(ch):
#     if 48 <= ord(ch) <= 57:
#         print("your character is a number.")
#     elif 65 <= ord(ch) <= 90:
#         print("your character is a uppercase letter.")
#     elif 97 <= ord(ch) <= 122:
#         print("your character is a lowercase letter.")
#     else:
#         print('Other')
# c = input('Enter a char: ')
# func(c)






# tell ==> موقعیت اشاره گر رو نشون میده
# seek ==> برای تغییر موقعیت هست
"""
متد seek  دوتا ارگومان داره
ارگومان اول: یه عددی میگیره و مشخص میکنه توی چه موقعیتی باشه
ارگومان دوم: سه تا مقدار داره 0 ==> ابتدای فایل | 1 ==> موقعیت فعلی فایل | 2 ==> انتهای فایل

text ==>  توی ارگومان ها  توی حالت متنی باید یکیش 0 باشه
"""

# ======================================================
# from os import linesep
# print(repr(linesep))
# ======================================================
# f = open(file='test2.txt', mode='wt')
#
# print(f.tell())
# f.write('a')
# print(f.tell())
# f.write('reza')
# print(f.tell())
# ======================================================
# f = open(file='test.txt', mode='rt', encoding='utf-8')
#
# print(f.tell())
# print(f.read(5))
# print(f.tell())
# ======================================================
# f = open(file='test.txt', mode='rb')
#
# print(f.tell())
# print(f.read())
# print(f.tell())
# ======================================================
# f = open(file='test.txt', mode='rt', encoding='utf-8')
#
# print(f.tell())
# print(f.read(4))
#
# f.seek(2)
# print(f.tell())
#
# print(f.read(4))
# ======================================================
# f = open(file='test.txt', mode='rb')
#
# print(f.tell())
# print(f.read(6))
# f.seek(2, 0)
# # f.seek(-3, 2)
# print(f.tell())
# print(f.read(6))
# ======================================================
# f = open(file='test.txt', mode='rt', encoding='utf-8')
#
# print(f.tell())
# print(f.read(2))
#
# f.seek(5, 0)  # باید یکیش صفر باشه
#
# print(f.tell())
# print(f.read(3))
# ======================================================
# توی mod=at اشاره گر میره انتهای فایل
# f = open(file='test.txt', mode='at', encoding='utf-8')
#
# print(f.tell())
# print(f.write('ab'))
#
# f.seek(0)
# print(f.tell())
# print(f.write('ze'))
#
# f.seek(0)
# print(f.tell())
# print(f.write('ze'))
# ======================================================

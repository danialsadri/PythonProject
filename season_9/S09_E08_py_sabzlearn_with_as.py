# context manager ==> دو تا متد داره : __enter__ , __exit__ | یه سری اشیایی هستند که قبل و بعد یه سری دستورایی میتونن کاری بکنن
# __enter__ , __exit__
"""
with ==> میاد روی اون کانتکث منیجر که در ادامه این ویس خواهیم نوشت
 ویس میاد اول این اینتر که اون کانتکث منیجر من داره صدا میزنه و با صدا اینتر یه سری کارهایی انجام میشه قبل اینکه دستورای داخل  بدنه ویس اجرا بشن
 بعد اینکه دستورای داخل بدنه ویس تموم شد ویس دوباره متد اگزیت رو صدا میزنه و سری کارهایی که اون کانتکث منیجر گفته بود بعد از انجام دستورات اجرا کن میاد دوباره اجرا میکنه
"""
# =======================================================================
# class A:
#     def __enter__(self):
#         print('start')
#         return 'ali'
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('end')
#
#
# with A() as x:
#     print(f'Hello {x}')
# =======================================================================
# فایل های من هم یه کاتکث منیجر هستن
#  متد اینتر داخل کاتکث منیجر چیزی که ریترن میکنه خود فایله


# with open(file='test.txt', mode='wt') as f:
#     f.write('hello')


# with open(file='test.txt', mode='rt') as f:
#     for line in f:
#         print(line, end='')


# with open(file='test.txt', mode='rt') as f1:
#     with open(file='new.txt', mode='wt') as f2:
#         for line in f1:
#             print(line, end='')
#             f2.write(line)


# with open(file='test.txt', mode='rt') as f1, open(file='new.txt', mode='wt') as f2:
#     for line in f1:
#         print(line, end='')
#         f2.write(line)
# =======================================================================

# مفهوم کروتون : دستور عملی هست که اتصال یه سری از ورودی ها به مجموعه ای از خروجی ها را رقم میزنه

# =============================================================
# def my_generator():
#     print('start!!!')
#     while True:
#         name = yield
#         print(f"my name is: {name}")
#
#
# g = my_generator()
# next(g)
# g.send('reza')
# g.send('reza')
# =============================================================
# def my_generator():
#     print('start!!!')
#     for i in range(10):
#         name = yield i
#         print(f"my name is: {name}")
#
#
# g = my_generator()
# print(next(g))
# print(g.send('reza'))
# print(next(g))
# print(g.send('ali'))
# print(next(g))
# print(g.send('akbar'))
# =============================================================
# from functools import wraps
# def coroutine(func):
#     @wraps(func)
#     def start(*args, **kwargs):
#         gn = func()
#         print(next(gn))
#         return gn
#     return start
#
# @coroutine
# def my_generator():
#     print('start!!!')
#     for i in range(3):
#         name = yield i
#         print(f"my name is: {name}")
#
#
# g = my_generator()
# print(g.send('reza'))
# print(g.send('ali'))
# print(g.send('hossein'))

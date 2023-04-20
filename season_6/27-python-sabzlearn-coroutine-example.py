# ========================================== 1 =====================================
# def cen_gen(words):
#     print('start!!!')
#     w = None
#     while True:
#         word = yield w
#         if word not in words:
#             w = word
#         else:
#             w = "*" * len(word)
#
#
# g = cen_gen(['khar', 'gav', 'gosaleh'])
# next(g)
# print(g.send('reza'))
# print(g.send('hasan'))
# print(g.send('gav'))
# ========================================== 2 =====================================
# def spl_gen(delimiter=' '):
#     print('Start!!!')
#     s = None
#     while True:
#         line = yield s
#         s = line.split(delimiter)
#
#
# g = spl_gen("-")
# next(g)
# print(g.send("ali-neda-sahel-hossein"))

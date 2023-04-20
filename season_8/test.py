# ==============================================================================
# import my_pkg.mod_1
# import my_pkg.mod_1 as mpm
# from random import randint
# from random import randint as r


# print(my_pkg.mod_1.func(5))
# print((npm.func(5)))
# print(my_pkg.mod_1)

# print(randint(10, 1000))
# print(r(10, 1000))
# =============================================================================
# import my_pkg.mod_1
# from my_pkg.mod_1 import func_1, func_2, name
# from my_pkg.mod_1 import *


# print(my_pkg.mod_1.func_1(5))
# print(my_pkg.mod_1.func_2('danialsadri'))


# f = my_pkg.mod_1.func_1
# print(f(10))


# print(my_pkg.mod_1.name)


# print(func_1(5))
# print(func_2('hello'))


# print(_func_3(2, 4))
# =============================================================================
# import my_pkg.mod_1
#
# print(my_pkg.mod_1.name)
# my_pkg.mod_1.name = 'mohammad'
# print(my_pkg.mod_1.name)
#
#
# from importlib import reload; reload(my_pkg.mod_1)
# print(my_pkg.mod_1.name)
# =============================================================================
# import my_pkg.mod_1
#
#
# print(my_pkg.mod_1.__name__)
# =============================================================================
# import sys
# print(sys.path)  # چاپ میکنه تمام مسیر هایی که الان این اسکریپت من اون مسیر هارو میشناسه
# =============================================================================
# from sys import path
#
# path.append(r'D:\py')
#
# for i in path:
#     print(i)
#
# import test
# test.func_1(5)
# =============================================================================
# from my_pkg import mod_1
# import builtins
# from my_pkg.mod_1 import func_1

# print(dir(func_1))
# print(mod_1.__file__)
# print(dir())
# print(dir(builtins))
# =============================================================================
# ----------------------------------------------
# import my_pkg
# print(my_pkg.__file__)
# ----------------------------------------------
# import my_pkg.mod_2
# my_pkg.mod_2.pow2(5)
# ----------------------------------------------
# =============================================================================
# import my_pkg.pk11.pk112.mod112 as mod
# from my_pkg.pk11.pk112.mod112 import pownx
# mod.pownx(2, 4)
# pownx(2, 4)
# =============================================================================
# from my_pkg.pk11.pk112.mod112 import *
# print(globals())
# ----------------------------------------------
# from my_pkg.pk11.pk112 import *
#
# print(globals())
# mod112.pownx(2, 4)
# mod113.print_str('danial')
# ----------------------------------------------
# from my_pkg.pk11.pk112 import mod112
#
# print(mod112.__doc__)
# print(help(mod112))
# ----------------------------------------------

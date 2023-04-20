# errors ==> strict | ignore | replace | backslashreplace | namereplace
# new_line ==> None | "" |

# =====================================================================
# f = open(file='test.txt', mode='rt', newline="")
# print(f.readlines())
# =====================  truncate  =====================================
# f = open(file='test.txt', mode='wt')
# f.write('danial\nsadri\n01')
# f.truncate(6)
# ======================================================================
# میاد مشخص میکنه وجود داره یا نه
# from os.path import exists
# if exists('test.txt'):
#     z = open(file='test.txt', mode='rt')
#     print(z.readlines())
# ======================================================================
# میاد فایل رو حذف میکنه
# from os import remove
# remove('new.txt')
# ======================================================================

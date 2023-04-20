# print(dir(str))
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
# 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
# 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
# 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
# ===================================================================================================================

# ---------------------------------------------------- ljust, rjust
# x = 'danial'
# print(x.ljust(10, '-'))
# print(x.rjust(10, '-'))
# ---------------------------------------------------- maketrans, translate
# s = 'Reza dolati'
# table = str.maketrans("d", '|', 'a')
# print(s)
# print(table)
# print(s.translate(table))
# ---------------------------------------------------- partition, rpartition
# s = 'danial 01 sadri'
# print(s.partition('01'))
# print(s.rpartition('s'))
# ---------------------------------------------------- removeprefix
# s = '----danial sadri 01----'
# print(s.removeprefix('----'))
# print(s.removesuffix('----'))
# ---------------------------------------------------- strip, rstrip, lstrip
# s = 'xzyyzxyxzyzxyyxyzyxyxz'
# print(s.removeprefix('xyz'))
# print(s.lstrip('xyz'))
# ---------------------------------------------------- rsplit, split
# s = 'danial, 01, sadri'
#
# print(s)
# print(s.split(',', 1))
# print(s.rsplit(',', 1))
# ---------------------------------------------------- splitlines
# s = 'danial\n01\nsadri'
# print(s)
# print(s.splitlines())
# print(s.splitlines(True))
# ---------------------------------------------------- swapcase
# s = 'DaNiAlSaDrI'
# print(s.swapcase())
# ---------------------------------------------------- zfill
# s = '123'
# print(s.zfill(10))
# ------------------------------
# minutes = '1'
# hour = '3'
# print(f"{minutes.zfill(2)}: {hour.zfill(2)}")

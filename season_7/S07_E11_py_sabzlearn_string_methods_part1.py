# print(dir(str))
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
# 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
# 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
# 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
# ===================================================================================================================

# ---------------------------------------------------- 'casefold' ==> رشته رو به حروف کوچک تبدیل میکنه
# x = 'DANIAL SADRI'
# print(x.casefold())
# ---------------------------------------------------- 'center'
# x = 'DANIAL'
# print(x.center(10, '|'))
# ---------------------------------------------------- 'expandtabs' ==> کاراکتر های تبی که تو رشته هست رو بااسپیس جایگزین میکنه
# x = 'DANIAL\tSADRI'
# print(x.expandtabs(20))
# ---------------------------------------------------- ==> 'format_map'
# dictionary = {'x': 20, 'y': 30}
# print("my name is {x} {y}".format_map(dictionary))
# ---------------------------------------------------- ==> 'index'
# x = 'Reza Dolati'
# print(x.index('a'))
# ---------------------------------------------------- ==> 'isalpha'
# x = 'RezaDolati'
# print(x.isalpha())
# ---------------------------------------------------- ==> 'isnumeric', 'isdecimal', 'isdigit'
# x = '12345678910'
# print(x.isnumeric())
# print(x.isdecimal())
# print(x.isdigit())
# ---------------------------------------------------- ==> isidentifier
# x = '_x_324'
# print(x.isidentifier())
# ---------------------------------------------------- ==> isidentifier
# x = 'danial\tsadri'
# print(x.isprintable())
# ---------------------------------------------------- ==> title | istitle
# x = 'danial sadri 01'
# print(x.title())
# print(x.istitle())

# ==================================================================
# f = open(file='test2.txt', mode='rt', encoding='utf-8')
# if f.writable():
#     print(f.write('ႈ'))
# if f.readable():
#     print(f.read())
# ==================================================================
# f = open(file='test2.txt', mode='wt', encoding='utf-8')
# list_ = ['danial', 'sadri', '01']
# dict_ = {'reza': 23, 'hasan': 45, 'akbar': 23}
# set_ = {'ali', 'akbari', '1303'}
# str_ = 'mohammad\nsadri\n98765'
# f.writelines(dict_)
# ==================================================================
# f = open(file='test2.txt', mode='rb')
# print(f.read())
# ==================================================================
# f = open(file='test2.txt', mode='rt', encoding='utf-8')
#
# print(f.read(15), end='')
# print(f.read(2), end='')
# ==================================================================
# f = open(file='test2.txt', mode='rb')
# print(f.read(6))  # به تعداد بایت ها میشماره میاره
# ==================================================================
# f = open(file='test2.txt', mode='rt')
# print(f.readline(3), end='')  # این لیمیت که مشخص کردم مشخص میکنه توی این خط چند تا بخونه
# print(f.readline(7), end='')
# print(f.readline(6), end='')
# print(f.readline(2), end='')
# ==================================================================
# f = open(file='test2.txt', mode='rt')
# print(f.readlines(14))  # به نزدیک ترین اندازه بافر گرد میکنه
# ==================================================================
# f = open(file='test2.txt', mode='rt')

# for _ in range(11):
#     print(f.readline(), end='')

# for _ in range(11):
#     print(f.read(5), end='')
# ==================================================================
# for line in open(file='test2.txt', mode='rt'):
#     print(line, end='')
# ==================================================================

# "{" [field_name] [ "!" conversation ] [ ":" format_spec ] "}"
# [[fill]align][sign][#][0][width][grouping_option][.precision][type]
# -----------------------------------------------------------------
# x = 22
# y = 33
# z = 324
# print("x is: {}\n y is: {}\n z is: {}".format(x, y, z))
# print("x is: {2}\n y is: {0}\n z is: {1}".format(x, y, z))
# -----------------------------------------------------------------
# d = {'a': 1, 'b': 2}
# print('a is: {a}\n b is: {b}'.format(a=d['a'], b=d['b']))
# -----------------------------------------------------------------
# x = 22
# y = 33
# print('x is: {}\n y is: {}'.format(*'re'))
# print('x is: {}\n y is: {}'.format(*[x, y]))
# -----------------------------------------------------------------
# "{" [field_name] [ "!" conversion ] [ ":" format_spec ] "}"
# [[fill]align][sign][#][0][width][grouping_option][.precision][type]

# field_name = اسم کلید  | ایندکس
# conversation = |  !s  |  !r  |  !a  |
# format_spec =         ==>
# type ==> |  :c  |  :s  |  :d  |  :o  |  :x  |  :e  |  :f  | :%  |
# .precision = نقطه اعشار
# grouping_option =  |  ,  |  _  |        اعداد بزرگ رو از هم جدا میکنه
#  width  = طول میدان
# 0 = جای خالی رو با صفر پر میکنه
# # ==>  بر مبنای باینری وقتی نشون میده اگه اون # رو بزاری اون صفر بی رو میزاره
# sign =    |  +  |  -  |  ==> اکه منفی بود خودش رو نشون میده و اگه مثبت باشه اسپیس میذاره
# [[fill]align] = fill میگه جای خالی رو با چی پر کن
# [[fill]align] = align میگه راست چین یا چپ چین یا وسط چین باشه


# print('x is: {0!s}'.format('reza'))
# print('x is: {0:#b}'.format(234))    <==  بر مبنای باینری وقتی نشون میده اگه اون # رو بزاری اون صفر بی رو میزاره
# print('x is: {0:+^-050,.5f}'.format(-323532444.77588647675))
# -----------------------------------------------------------------
# print('x is: {0:{fill}{align}{sign}{width}}'.format(34, fill='*', align='>', sign='+', width='10'))

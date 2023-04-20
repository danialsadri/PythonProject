# x = 2
# y = 4
# z = 3
#
# print(divmod(x, y))  # x= حاصل ایکس تقسیم بر وای  |n  حاصل ایکس باقیماندش به وای ==> (x // y, x % y)
# print((pow(x, y, z)))  # x به توان y  میرسونه |n و حاصل به z رو حساب میکنه
# print(round(x))  # عدد رو روند میکنه
# print(abs(x))  # قدر مطلق رو حساب میکنه
# ===================================================================
# print(dir(int))
# 'as_integer_ratio','bit_count','bit_length','conjugate','denominator','from_bytes','imag','numerator','real','to_bytes'
# x = 5
# print(x.as_integer_ratio())  # نسبت رو پیدا میکنه
# print(x.bit_count())  # نشون میده وقتی عددم باینری باشه چند تا بیت یک داره
# print(x.bit_length())  # تعداد بیت هایی که برای نوشتن اون عدد نیاز داریم
# print(x.real)
# print(x.imag)
# print(x.conjugate())
# print(x.denominator)  # مخرج یه عددیو نشون میده
# print(x.numerator)  # صورت یه کسریو نشون میده
# print(x.to_bytes(3, byteorder='big', signed=False))  # عددی که دارم رو تبدیل میکنه به ارایه ای از بایت ها
# print(int.from_bytes(b'\x00\x00\x05', byteorder='big'))  # عدد باینری که دارم تبدیل میکنه به عدد دسیمال
# ===================================================================
# print(dir(float))
# 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real'

# x = 5.0

# print(x.hex())  # عدد مبنای 10 رو تبدیل میکنه به هکسا دسیمال
# print(x.fromhex('0x1.5333333333333p+2'))  # عدد هکسا دسیمال رو تبدیل میکنه به مبنای 10
# print(x.is_integer())  # عدد صحیح هست یا نه

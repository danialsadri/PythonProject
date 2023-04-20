# underscore:
# 1- استفاده از (_) به تنهایی
# 2- استفاده از (_) قبل از اسم یک متغیر یا متد یا اتریبیوت
# 3- استفاده از (_) بعد از اسم یک متغیر یا متد یا اتریبیوت
# 4- استفاده از (__) قبل از اسم یک متغیر یا متد یا اتریبیوت
# 5- استفاده از (__) قبل  و  بعد از اسم یک متغیر یا متد یا اتریبیوت


# public ==> name
# private ==> __name ==> name mangling
# protected ==> _name


# -----------  1  ----------------
# for _ in range(10):
#     print('hello')
# --------------------------------

# -----------  1  ----------------
# name, age = ('ali', 12)
# print(f"{name} {age}")

# name, _ = ('ali', 12)
# print(f"{name} {_}")
# --------------------------------

# -----------  1  ----------------
# توی حالت تعاملی هستش که اخرین مقدار نوشته رو توی خودش ذخیره میکنه
# --------------------------------

# -----------  2  ----------------
# class User:
#     def __init__(self, name="", phone=""):
#         self._user_id = id(self)
#         self.name = name
#         self.phone = phone
#
#
# ali = User('ali', '0939')
#
# print(f"{ali._user_id} - {ali.name} - {ali.phone}")
# --------------------------------

# -----------  2  ----------------
# from point import *
#
# print(y)
# print(_x)
# --------------------------------

# -----------  3  ----------------
# min_ = 10
# print(min_)
# --------------------------------

# -----------  4  ----------------
# class User:
#     def __init__(self, name="", phone=""):
#         self.__user_id = id(self)
#         self.name = name
#         self.phone = phone
#         self.plus = '+' + str(self.__user_id)
#
#
# class Account(User):
#     def __init__(self):
#         super().__init__()
#         self.__user_id = "12345"
#
#
# ali = User('ali', '09391234567')
# ali_account = Account()
#
# print(dir(ali))
# print(dir(ali_account))
#
# print(f"{ali._User__user_id} - {ali.name} - {ali.phone}")
# print(f"{ali_account._Account__user_id}")
# --------------------------------

# -----------  5  ----------------
# """
# اون متغییر هایی که دو تا اندراسکور قبل و بعدش دارن جز متد های خاص هستند بهشون میگیم اسپشیول متد یا مجیک متد و این متد هارو پایتون رزرو کرده برای یه کار و وظیفه خاصی
#  و ما نباید برای متد های عادی ازش استفاده کنیم
# """
# --------------------------------


# -------------getter & setter-------------------
# class User:
#     def __init__(self, name='----', phone='----'):
#         self.user_id = id(self)
#         self.name = name
#         self.__phone = phone
#
#     def set_phone(self, phone):
#         if (len(phone) == 11) and (phone.isdigit()):
#             self.__phone = phone
#
#     def get_phone(self):
#         return self.__phone
#
#
# ali = User()
# ali.set_phone('09131234567')
# number = ali.get_phone()
# print(number)
# --------------------------------

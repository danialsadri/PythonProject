"""
از تابع چه زمانی استفاده میکنیم؟؟
زمانی استفاده میکنیم قراره یک عمل یک اقدام یک کاری که باید انجام بشه رو بنویسید معمولا فعل هستش
"""
"""
زمانی هست میخام یک صفتی داشته باشم یک توصیفی یک اسمی داشته باشم از اتریبیوت و پراپرتی استفاده میکنم
"""
# ===========================================================================================================
# class Color:
#     def __init__(self, rgb, name):
#         self.rgb = rgb
#         self.name = name
#
#     def _set_name(self, name):
#         if name:
#             self._name = name
#         else:
#             raise ValueError(f'Invalid name {name!r}')
#
#     def _get_name(self):
#         """ new doc... """
#         return self._name
#
#     def _del_name(self):
#         print('Deleting...')
#         del self._name
#
#     # -------------------------------
#     name = property()
#     name = name.setter(_set_name)
#     name = name.getter(_get_name)
#     name = name.deleter(_del_name)
#     # -------------------------------
#     # name = property(fset=_set_name, fget=_get_name, fdel=_del_name, doc='new...')
#     # -------------------------------
#
#
# c = Color(rgb=0x42534, name='red')
# c.name = "ali"
# print(c.name)
# del c.name
# # help(c)
# ===========================================================================================================
# class Color:
#     def __init__(self, rgb, name):
#         self.rgb = rgb
#         self.name = name
#
#     @property
#     def name(self):
#         """ new doc... """
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         if name:
#             self._name = name
#         else:
#             raise ValueError(f'Invalid name {name!r}')
#
#     @name.deleter
#     def name(self):
#         print('Deleting...')
#         del self._name
#
#
# c = Color(rgb=0x42534, name='red')
# c.name = "ali"
# print(c.name)
# del c.name
# help(c)
# ===========================================================================================================
"""
فرض کنید برای کلاس لیست معمولی خودم یه کلاس لیست جدید داشته باشم ولی با این قابلیت که بتونه میانگین تمام عناصرش رو چاپ کنه
"""
"""
درسته رفتار داره برای محاسبه کردنش و در نهایت یک حالت اتریبیوت تر میگیره و مثل صفت براش میمونه 
 درسته یک کار انجام میده ولی در نهایت کاری انجام میده صفته
"""
"""
پراپرتی ها خیلی شبیه به اتریبیوت ها هستن تفاوتشون اینه که ما معمولا قبل اینکه اون اتریبیوت رو داشته باشیم یه تغییرات کوچیک روش انجام میدیم
"""
# --------------------------------------------------------
# list_1 = [1, 2, 3, 4, 5]
#
#
# class NewList(list):
#     @property
#     def ave(self):
#         return sum(self) / len(self)
#
#
# list_2 = NewList((1, 2, 3, 4))
# print(list_1)
# print(list_2)
# print(list_2.ave)
# --------------------------------------------------------

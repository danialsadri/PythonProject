# ======================================================================================================================
# class Parent:
#     def __init__(self, child_name, father_name, mother_name):
#         self.child_name = child_name
#         self.father_name = father_name
#         self.mother_name = mother_name
#
#     @property
#     def child_name(self):
#         """ new doc... """
#         return self._child_name
#
#     @child_name.setter
#     def child_name(self, child_name):
#         if 0 < len(child_name) < 15:
#             self._child_name = child_name
#         else:
#             raise ValueError(f'Invalid name {child_name!r}')
#
#     @child_name.deleter
#     def child_name(self):
#         print('Deleting...')
#         del self._child_name
#
#     @property
#     def father_name(self):
#         """ new doc... """
#         return self._father_name
#
#     @father_name.setter
#     def father_name(self, father_name):
#         if 0 < len(father_name) < 15:
#             self._father_name = father_name
#         else:
#             raise ValueError(f'Invalid name {father_name!r}')
#
#     @father_name.deleter
#     def father_name(self):
#         print('Deleting...')
#         del self._father_name
#
#     @property
#     def mother_name(self):
#         """ new doc... """
#         return self._mother_name
#
#     @mother_name.setter
#     def mother_name(self, mother_name):
#         if 0 < len(mother_name) < 15:
#             self._mother_name = mother_name
#         else:
#             raise ValueError(f'Invalid name {mother_name!r}')
#
#     @mother_name.deleter
#     def mother_name(self):
#         print('Deleting...')
#         del self._mother_name
#
#
# parent = Parent(child_name='reza', father_name='mahdi', mother_name='neda')
# parent.child_name = "ali"
# parent.father_name = "hasan"
# parent.mother_name = "mahsa"
#
# print(parent.__dict__)
# ======================================================================================================================
"""
دسکریپتور ها در واقع کلاس هایی هستند که یکی از متد های گت و ست و دلیت رو برای ما اورراید میکنن
یعنی اگه بیاین  هر کدوم از متد های گت و ست و دلیت رو اور راید کنن که جز متد های داخلی پایتونه اون وقت اون کلاس ما میشه یک کلاس دسکریپتور
"""
"""
وظیفه دسکریپتور چیه?? 
وظیفشون اینه که یه سری رفتار هارو برای اتریبیوت های ما ایجاد کنن
"""
"""
از دسکریپتور فقط برای کلاس اتریبیوت استفاده میشود 
"""
"""
 name = NameField() یک ابجکت از کلاس نیم فیلد ساختم به اسم نیم ولی چون برای کلاس بالایی یک متد گت و ست و دلیت رو نوشتم
  حالا وقتی میخام بگیرمش اون چیزی که برای گت نوشتم رو انجام میده و برای ست و دلیت هم همینطور
"""


# -------------------------------------------------------------------------------------
# class NameField:
#     def __init__(self, name=None):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         # return self.name
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if 0 < len(value) < 15:
#             # self.name = value
#             instance.__dict__[self.name] = value
#         else:
#             raise ValueError(f"Invalid name {value!r} (len:{len(value)})")
#
#     def __delete__(self, instance):
#         print('Deleting...')
#         # del self.name
#         del instance.__dict__[self.name]
#
#
# class Parent:
#     child_name = NameField("child_name")
#     father_name = NameField("father_name")
#     mother_name = NameField("mother_name")
#
#     def __init__(self, child, father, mother):
#         self.child_name = child
#         self.father_name = father
#         self.mother_name = mother
#
#
# p = Parent(child='reza', father='mahdi', mother='mahboobe')
# print(p.child_name)
# print(p.mother_name)
# print(p.father_name)
# print(p.__dict__)
# -------------------------------------------------------------------------------------
# class NameField:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         # return self.name
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if 0 < len(value) < 15:
#             # self.name = value
#             instance.__dict__[self.name] = value
#         else:
#             raise ValueError(f"Invalid name {value!r} (len:{len(value)})")
#
#     def __delete__(self, instance):
#         print('Deleting...')
#         # del self.name
#         del instance.__dict__[self.name]
#
#
# class Parent:
#     child_name = NameField()
#     father_name = NameField()
#     mother_name = NameField()
#
#     def __init__(self, child, father, mother):
#         self.child_name = child
#         self.father_name = father
#         self.mother_name = mother
#
#
# p = Parent(child='reza', father='mahdi', mother='mahboobe')
# print(p.child_name)
# print(p.father_name)
# print(p.mother_name)
# p.mother_name = 'mahsa'
# print(p.mother_name)
# del p.mother_name
# -------------------------------------------------------------------------------------

# ======================================================================================================================

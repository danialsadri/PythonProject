"""
data class ==> میگه شما ممکنه بعضی وقتا یک کلاسی داشته باشی که صرفا میخوای یسری اتریبیوت هایی توش ذخیره کنی و نمیخوای
یک کلاسی پیچیده و کلی داشته باشی
"""

from dataclasses import dataclass, InitVar
from typing import ClassVar


# -----------------------------------------------------------------
# @dataclass
# class Person:
#     name: str
#     family: str
#     age: int
#     gender: InitVar[str]
#
#     def __post_init__(self, gender):
#         # if self.age < 0:
#         # self.age = 0
#         if gender == 'man':
#             self.name += '*'
#
#
# p = Person(name='reza', family='dolati', age=27, gender='man')
# print(p)
# p.age = 30
# print(p)
# -----------------------------------------------------------------
# @dataclass
# class Person1:
#     name: str = 'danial'
#     family: str = 'sadri'
#     age: int = 25
#
#
# @dataclass
# class Person2(Person1):
#     name2: str = 'danial'
#     family2: str = 'sadri'
#     age2: int = 25
#
#
# p = Person2(name='mohammad', family='dolati', age=25, name2='taha', family2='akbari', age2=30)
# print(p)
# -----------------------------------------------------------------
# @dataclass
# class Person:
#     name: str = 'danial'
#     family: str = 'sadri'
#     age: ClassVar[int] = 0
#
#
# p = Person('danial', 'sadri')
# print(p)
# print(Person.age)
# -----------------------------------------------------------------

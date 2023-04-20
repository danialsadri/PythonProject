# operator overloading ==> سربار گذاری عملگر ها
"""
یعنی یک عملگر بسته به اینکه با چه شی ای کار میکنه میتونه رفتار متفاوت تری رو داشته باشه
"""
# ========================================================================================
# print(1 + 2)
# print('danial' + 'sadri')  # عملگر همونه ولی رفتاری که داره نشون میده متفاوته بسته به رشته یا عدد یا کامپلکس
# print('reza' + 'dolati')  # پشت صحنه این اتفاق متد هایی هست که برای این عملگر ها داخل کلاسشون تعریف شده
# ========================================================================================
# class Person:
#     def __init__(self, first_name, last_name, age, national_code):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.national_code = national_code
#
#     def __str__(self):
#         return f"{self.first_name} - {self.last_name} - {self.age} - {self.national_code}"
#
#     #
#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.first_name}', '{self.last_name}', {self.age}, {self.national_code})"
#
#     def __add__(self, other_person):
#         return self.age + other_person.age
#
#     def __lt__(self, other_person):
#         return self.age < other_person.age
#
#     def __eq__(self, other_person):
#         return self.national_code == other_person.national_code
#
#
# person_1 = Person(first_name='ali', last_name='mohammadi', age=20, national_code='5039876543')
# person_2 = Person(first_name='danial', last_name='sadri', age=17, national_code='5039876543')
#
# print(person_1 + person_2)
# print(person_1 < person_2)
# print(person_1 == person_2)
# ========================================================================================

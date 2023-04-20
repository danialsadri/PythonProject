# ===============================================  Composition =========================================================
"""
چجوری این رو با پیاده سازی نشون دادیم؟؟؟
 ابجکته همینجا ایجاد شد
یعنی داخل همون کلاسم نشون داده که ایجاد کنه مثلا مثال پایین اگه کلاس برگه امتحانی نابود بشه سوالاتشم نابود میشه
"""
# class Question:
#     def __init__(self, q: str, a: list):
#         self.q = q
#         self.a = a
#
#
# class ExamPaper:
#     def __init__(self):
#         self.question = Question(q='what is your name???', a=['reza', 'ali', 'mohammad', 'danial'])
#
#     def __str__(self):
#         return f"{self.question.q}\n{self.question.a}"
#
#
# e = ExamPaper()
# del e
# print(e)
# ===============================================  aggregation =========================================================
"""
مثل دانشجو و دانشگاه میمونه دانشگاه بدون دانشجو  هم دانشگاهه و دانشجو هم بدون دانشگاه باز یک شخصیت مستقله
جفتشون کنار هم وجود دارن مستقل وجود دارن 
"""


# class Student:
#     def __init__(self, name, number):
#         self.name = name
#         self.number = number
#
#     def __str__(self):
#         return f"{self.name}: {self.number}"
#
#
# class University:
#     def __init__(self, students: list[Student]):
#         self.students = students
#
#
# st = [Student('danial', '1234'), Student('mohammad', '4321')]
# university = University(students=st)
# for student in university.students:
#     print(student)
# ======================================================================================================================

"""
از اسم کلاس  استفاده میکنم و ابجکت رو بهش میفرستم و متد اینیت رو صدا میزنم و مقدار دهی میکنم
یعنی بجای اینکه از تابع سوپر استفاده کنم میام اسم کلاس رو مینویسم و متد اینیت اش رو صدا میزنم و برای اینکه بفهمیم برای کدام ابجکت باید اینیتش رو صدا بزنم سلف رو بهش میفرستم و اون مقدار رو هم بهش میفرستم
"""


class SuperClass1:
    def __init__(self, p1):
        self.p1 = p1


class SuperClass2:
    def __init__(self, p2):
        self.p2 = p2


class SubClass(SuperClass1, SuperClass2):
    def __init__(self, p1, p2, p3):
        SuperClass1.__init__(self, p1)
        SuperClass2.__init__(self, p2)
        self.p3 = p3


obj = SubClass(1, 2, 3)
print(obj.p1)
print(obj.p2)
print(obj.p3)

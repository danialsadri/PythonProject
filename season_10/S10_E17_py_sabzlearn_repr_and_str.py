# str ==> string ==> __str__
# repr ==> representation ==> __repr__
"""
ما از str زمانی استفاده میکنیم که کاربر نهایی قراره ببینه ولی repr برای توسعه و دیباگ استفاده میشه
معمولا repr به شکلی هست که با استفاده از اون دوباره ابجکت رو بازسازی کنید
"""


# دیفالت حالت تعاملی repr هستش

# print(str("ali"))
# print(repr("ali"))

# from datetime import datetime
# print(str(datetime.now()))
# print(repr(datetime.now()))
# print(datetime(2023, 3, 18, 11, 0, 3, 359784))

# وقتی توی کلاسی str تعریف نکرده باشم بصورت دیفالت repr رو نشون میده یعنی str داخل خودش repr  رو صدا میزنه

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.age}"

    #
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.first_name}', '{self.last_name}', {self.age})"


person = Person(first_name='ali', last_name='mohammadi', age=17)

print(str(person))
# print(person.__str__())
print(repr(person))
# print(person.__repr__())

# print(f"{person.first_name} - {person.last_name} - {person.age}")

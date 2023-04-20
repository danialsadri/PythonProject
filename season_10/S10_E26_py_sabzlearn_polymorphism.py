"""
polymorphism ==> مفهومش چند شکلی بودن رو برای ما میگه و میگه که یک اسم داریم ولی دارای رفتار و شکل های مختلف هست
"""


# =========================================================================================

# ------------------------------------
# ما یک اپراتور داریم عملگر همونه ولی بر اساس اینکه چه ابجکت هایی چه تایپ هایی رو با هم جمع میکنه رفتار متفاوتی رو از خودش نشون میده
# print('r' + 'd')
# print(2 + 3)
# print(3 + 2j + 4j)
# ------------------------------------

# ------------------------------------
# کلا یک اسم رو به کار بردم ولی به چند شکل مختلف کار کرد بسته به اینکه اون ابجکت که میخاد باهاش کار کنه چه نوعی یا تایپی هست
# print(len('danial sadri'))
# print(len([1, 2, 3, 4, 5]))
# print(len({'a': 1, 'b': 2, 'c': 3}))
# ------------------------------------

# ------------------------------------
# یه تابع نوشتم اسم ثابته ولی رفتار میتونه بسته به ابجکت ها متفاوت باشه
# def add(x, y):
#     print(x + y)
#
#
# add(1, 2)
# add('r', 'd')
# ------------------------------------

# =========================================================================================
# چند ریختی توی وراثت

# ------------------------------------
#   دو کلاس مختلف دارم ولی دو متد دارم با اسم های یکسان ولی پیاده سازی متفاوت یا رفتار متفاوت
# class Cat:
#     def __init__(self, name="", color=""):
#         self.name = name
#         self.color = color
#
#     def info(self):
#         print(f"hello, I am a cat. My name is {self.name}, I am {self.color}")
#
#     def make_sound(self):
#         print("meow...")
#
#
# class Cow:
#     def __init__(self, name="", color=""):
#         self.name = name
#         self.color = color
#
#     def info(self):
#         print(f"hello, I am a cow. My name is {self.name}, I am {self.color}")
#
#     def make_sound(self):
#         print("Moo...")
#
#
# cat = Cat('jaki', 'black')
# cow = Cow('Gavi', 'brown')
#
#
# for animal in [cat, cow]:
#     animal.make_sound()
#     animal.info()
# ------------------------------------

# ------------------------------------
# یک فانکشن رو نوشتم که یک ابجکت رو میگیره و بدون اینکه براش مهم باشه اون ابجکت من چیه مثلا گربه هس
# یا گاو و ... و میگه تا زمانی که این ها متدی به نام اینفو و میک ساند دارن برای اینکه نوعش برای من چی هستش اهمیتی نداره
# از اسم مشترکی استفاده میکنم ولی رفتار متفاوتی رو میبینم

# class Cat:
#     def __init__(self, name="", color=""):
#         self.name = name
#         self.color = color
#
#     def info(self):
#         print(f"hello, I am a cat. My name is {self.name}, I am {self.color}")
#
#     def make_sound(self):
#         print("meow...")
#
#
# class Cow:
#     def __init__(self, name="", color=""):
#         self.name = name
#         self.color = color
#
#     def info(self):
#         print(f"hello, I am a cow. My name is {self.name}, I am {self.color}")
#
#     def make_sound(self):
#         print("Moo...")
#
#
# def func(obj):
#     obj.info()
#     obj.make_sound()
#
#
# cat = Cat('jaki', 'black')
# cow = Cow('Gavi', 'brown')
#
# func(cat)
# func(cow)
# ------------------------------------

# =========================================================================================
# چند ریختی در ارث بری
# همون متد هست همون اسم هست ولی بسته به اینکه چه ابجکتی هست داره رفتار متفاوتی از خودش نشون میده

# ------------------------------------
# class Animal:
#     def __init__(self, name="", color=""):
#         self.name = name
#         self.color = color
#
#     def info(self):
#         print(f"hello, I am a animal. My name is {self.name}, I am {self.color}. ")
#
#     def make_sound(self):
#         print("I can make sounds. ")
#
#
# class Cat(Animal):
#     def __init__(self, name="", color=""):
#         super().__init__(name, color)
#
#     def info(self):
#         print(f"hello, I am a cat. My name is {self.name}, I am {self.color}. ")
#
#     def make_sound(self):
#         print("meow...")
#
#
# class Cow(Animal):
#     def __init__(self, name="", color=""):
#         super().__init__(name, color)
#
#     def info(self):
#         print(f"hello, I am a cow. My name is {self.name}, I am {self.color}. ")
#
#     def make_sound(self):
#         print("Moo...")
#
#
# animal = Animal()
# cat = Cat('jaki', 'black')
# cow = Cow('Gavi', 'brown')
#
# animal.make_sound()
# cat.make_sound()
# cow.make_sound()
#
# animal.info()
# cat.info()
# cow.info()
# ------------------------------------

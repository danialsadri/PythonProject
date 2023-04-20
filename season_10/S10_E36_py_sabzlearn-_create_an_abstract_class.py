from abc import ABC, ABCMeta, abstractmethod

"""
نکته ۱- کلاس های ابسترکت من اینجوری نیست که فقط متد های ابسترکت داشته باشن یعنی مشکلی نداره یه متد خیلی عادی هم بنویسم 

نکته۲- از کلاس های ابسترکت نمیشه ابجکت ایجاد کرد

نکته ۳- هیچ الزامی نداره که متد های ابسترکت خالی باشن میتونن مقدار دیفالت داشته باشن ولی رایجه که خالی باشن 

نکته ۴- کلاس های ابسترکت میتونن از هم ارث بری کنن ولی نکته مهم اینجاس که وقتی کلاس دیگه رو دارم از این ارث بری میکنم 
تا زمانی که اون کلاسی که داره از این ارث بری میکنه همه متد های ابسترکت اون رو پیاده سازی نکرده خودش یک کلاس انتزاعیه 
"""


# =====================================================================
# class Vehicle(metaclass=ABCMeta):
#
#     @abstractmethod
#     def move(self):
#         """this method should be implemented!!!"""
#
#     @abstractmethod
#     def repair(self):
#         """this method should be implemented!!!"""
# =====================================================================
# Abstract Base Class
# class Vehicle(ABC):
#
#     @abstractmethod
#     def move(self):
#         """this method should be implemented!!!"""
#
#     @abstractmethod
#     def repair(self):
#         """this method should be implemented!!!"""
#
#     def class_name(self):
#         print(self.__class__)
#
#
# # Abstract Base Class
# class LandVehicle(Vehicle):
#     @abstractmethod
#     def brake(self):
#         """this method should be implemented!!!"""
#
#
# # Abstract Base Class
# class AirVehicle(Vehicle):
#     @abstractmethod
#     def eject(self):
#         """this method should be implemented!!!"""
#
#
# # Concrete Class
# class Car(LandVehicle):
#     def move(self):
#         print('Driving!!!')
#
#     def repair(self):
#         print('under repair')
#
#     def brake(self):
#         print('Braking...')
#
#
# # Concrete Class
# class AirPlane(AirVehicle):
#     def move(self):
#         print('Flying!!!')
#
#     def repair(self):
#         print('under repair')
#
#     def eject(self):
#         print('Ejecting...')
#
#
# c = Car()
# c.move()
# c.repair()
# c.brake()
# c.class_name()
#
# print('-' * 40)
#
# a = AirPlane()
# a.move()
# a.repair()
# a.eject()
# a.class_name()
# =====================================================================

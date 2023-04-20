"""
: دو نوع خطا خیلی مهم داریم
1- خطاهای ساختاری یا سینتکس ارور ها: خطاهایی هستند که مفسر شما قبل اینکه برنامه شما رو اجرا کنه تشخیص میده
2- استثناها: خطاهایی هستند که موقعی که دارین کدتون رو اجرا میکنین خطا رخ میده
"""
# اگر توی ترای و اکسپت  قسمت ترای جایی که به ارور بخوری خط های بعد ان اجرا نمیشن
# else: زمانی اجرا میشه که هیچ گونه استثنایی ندارم
# finally: هر چیزی داخل فاینالی نوشته بشه چه استثنا داشته باشم چه استثنا نداشته باشم باید اجرا بشه

try:
    x = int(input("x: "))
    y = int(input('y: '))
    print(f"x / y = {x / y}")
    print('test')
    if y == 10:
        raise NameError('goodbye!!!')

except ZeroDivisionError:
    print('ZeroDivisionError!!!')
    x = int(input("x: "))
    y = int(input('y: '))
    print(f"x / y = {x / y}")

except ValueError:
    print('ValueError!!!')
    x = int(input("x: "))
    y = int(input('y: '))
    print(f"x / y = {x / y}")

except:
    print('Unknown Error!!!')

else:  # زمانی اجرا میشه که هیچ گونه استثنایی ندارم
    print("The End")

finally:  # هر چیزی داخل فاینالی نوشته بشه چه استثنا داشته باشم چه استثنا نداشته باشم باید اجرا بشه
    print('good job!!!')

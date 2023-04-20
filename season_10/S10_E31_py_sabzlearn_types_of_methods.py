from datetime import datetime, timedelta

# Instance Method
"""
ما یکی از متد هایی که داریم اینستنس متد هست یعنی متد اون ابجکت یا اینستنس
این متد چه متدیه؟؟؟ متدهایی هست که الان استفاده کردیم رایج ترین متد های ما هست و برای دستیابی و استفاده از اینستنس اتریبیوت ها ازش استفاده میشه.
 اون متدی که به این اینستنس اتریبیوت ها میتونه دسترسی داشته باشه تغییر بده بخونه بهشون میگیم اینستنس متد ها 
"""
"""
ویژگی های اینستنس متد ها چیه ؟؟
به عوان ورودی سلف رو میگیره
"""
# Class Method
"""
متد هایی هستند که به ابجکت و اتریبیوت ابجکت دسترسی ندارند  اصلا اهمیتی نداره چه ابجکتی هست 
یه چیزی هست که مخصوص کلاس هست اصلا براش اهمیت نداره ابجکت چی باشه پس یه چیز عمومی تره یچیزیه که توی همه ابجکت ها با هم استفاده میشه
و اختصاصی نیست مثلا متد هایی که قراره به یک اتریبیوت کلاس دسترسی داشته باشن  
"""
# Static Method
"""
زمان  هایی هست من یه متدی خیلی نیاز دارم توی این کلاس استفاده کنم و اگه کاربر این کلاس رو ایپورت کرد
 میخام یه متدی هم حتما ایپورت بشه و از اون استفاده کنه ولی نه کلاس رو کاری داره و نه ابجکت رو کاری داره 
"""
"""
اگه یه متدی نوشتم که توی چند تا کلاس قراره استفاده بشه
  خب بیرون کلاس ها مینوسم و ازش استفاده میکنم ولی اگه مخصوص یه کلاسی بود توی اون کلاس به عنوان استتیک متد مینوسم
   و میگم نه سلف نه سی ال اس رو میگیره
"""


class Product:
    def __init__(self, product_name, price, off):
        self.product_name = product_name
        self.price = price
        self.off = off

    def __str__(self):
        return self.product_name


class Comment:
    website_name = 'sabzlearn.ir'

    # Instance Method
    def __init__(self, product, name, description, like, dislike):
        self.product = product
        self.name = name
        self.description = description
        self.date = datetime.now()
        self.like = like
        self.dislike = dislike

    # Instance Method
    def show(self):
        print(f"product: {self.product}\n"
              f"name: {self.name}\n"
              f"description: {self.description}\n"
              f"date: {self.date}\n"
              f"like: {self.like} and dislike: {self.dislike}\n")

    @classmethod
    def info(cls):
        print(f"website name: {cls.website_name}")

    @classmethod
    def censorship(cls, product, name, description, like, dislike):
        print('this comment was censored!!!')
        censor_description = description.replace('بیشعور', '****')
        return cls(product, name, censor_description, like, dislike)

    @staticmethod
    def elapsed_time(time):
        print(datetime.now() - time)


python_course = Product(product_name='python expert', price=0, off=0)

comment_1 = Comment(product=python_course, name='danial', description='دوره بسیار خوبی بود!!!', like=100, dislike=0)
comment_1.show()
print('-' * 50)

# comment_1.info()
Comment.info()
print('-' * 50)

comment_2 = Comment.censorship(product=python_course, name='danial', description='دوره بسیار بیشعور بود!!!', like=100, dislike=0)
comment_2.show()
print('-' * 50)

# Comment.elapsed_time(comment_2.date - timedelta(days=2, hours=30, seconds=5))
Comment.elapsed_time(comment_2.date)
print('-' * 50)


# --------------------------
# class A(Comment):
#     pass
#
#
# print(dir(A))
# ---------------------------

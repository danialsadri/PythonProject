# class BaseClass:
#     num_base_calls = 0
#
#     def __init__(self, a, b, **kwargs):
#         self.a = a
#         self.b = b
#
#     def call_me(self):
#         print('Calling method on BaseClass!!!')
#         self.num_base_calls += 1
#
#
# class LeftSubClass(BaseClass):
#     num_left_calls = 0
#
#     def __init__(self, c, **kwargs):
#         super().__init__(**kwargs)
#         self.c = c
#
#     def call_me(self):
#         super().call_me()
#         print('Calling method on LeftSubClass!!!')
#         self.num_left_calls += 1
#
#
# class RightSubClass(BaseClass):
#     num_right_calls = 0
#
#     def __init__(self, d, e, f, **kwargs):
#         super().__init__(**kwargs)
#         self.d = d
#         self.e = e
#         self.f = f
#
#     def call_me(self):
#         super().call_me()
#         print('Calling method on RightSubClass!!!')
#         self.num_right_calls += 1
#
#
# class SubClass(LeftSubClass, RightSubClass):
#     num_sub_calls = 0
#
#     def __init__(self, g, **kwargs):
#         super().__init__(**kwargs)
#         self.g = g
#
#     def call_me(self):
#         super().call_me()
#         print('Calling method on SubClass!!!')
#         self.num_sub_calls += 1
#
#
# s = SubClass(a=1, b=2, c=3, d=4, e=5, f=6, g=7)
# s.call_me()
# print(f"{s.num_sub_calls} {s.num_left_calls} {s.num_right_calls} {s.num_base_calls}")
# print(f"a={s.a}  b={s.b}  c={s.c}  d={s.d}  e={s.e}  f={s.f}  g={s.g}")
# ============================================================================================================
class UserList(list["User"]):
    def search(self, username: str) -> list["User"]:
        matching_users: list["User"] = []
        for user in self:
            if username in user.username:
                matching_users.append(user)
        return matching_users

    def append(self, obj) -> None:
        if not isinstance(obj, User):
            raise TypeError('this list only accepts User')
        return super().append(obj)


class User(object):
    all_users: list["User"] = UserList()

    def __init__(self, username: str, email: str, password: str, **kwargs) -> None:
        self.username = username
        self.email = email
        self.password = password
        User.all_users.append(self)

    def __str__(self):
        return f"{self.username} - {self.email} - {self.password}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.username!r}, {self.email!r}, {self.password!r})"


class Buyer(User):
    def __init__(self, phone: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.phone = phone

    def __str__(self):
        return f"{self.username} - {self.email} - {self.password} - {self.phone}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.username!r}, {self.email!r}, {self.password!r}, {self.phone!r})"


class Seller(User):
    def __init__(self, shaba, **kwargs):
        super().__init__(**kwargs)
        self.shaba = shaba

    def order(self, order: "Order") -> None:
        print(f"{self.username}, From your products, {order} was sold!")

    def __str__(self):
        return f"{self.username} - {self.email} - {self.password} - {self.shaba}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.username!r}, {self.email!r}, {self.password!r}, {self.shaba!r})"


class SellerAndBuyer(Seller, Buyer):
    def __init__(self, score, **kwargs):
        super().__init__(**kwargs)
        self.score = score

    def __str__(self):
        return f"{self.username} - {self.email} - {self.password} - {self.phone} - {self.shaba} - {self.score}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.username!r}, {self.email!r}, {self.password!r}, {self.phone!r}, {self.shaba!r} {self.score})"


def main():
    user_account = User(username='akbar', email='akbar@gmail.com', password='1234')
    buyer_account = Buyer(username='danial', email='danial@gmail.com', password='5678', phone='09391234567')
    seller_account = Seller(username='mohammad', email='mohammad@gmail.com', password='9012', shaba='IR1234')
    seller_buyer_account = SellerAndBuyer(username='hossein', email='hossein@gmail.com', password='5466', phone='09131234567', shaba='IR1234', score='10')
    print(f"user_account= {user_account}")
    print(f"buyer_account= {buyer_account}")
    print(f"seller_account= {seller_account}")
    print(f"seller_buyer_account= {seller_buyer_account}")
    print(User.all_users)


if __name__ == "__main__":
    main()

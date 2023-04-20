# override ==> تغییر یا جایگزینی یک متد از سوپر کلاس با متد جدید که هم اسم اون هست توی زیر کلاس
# super method ==>  زیر کلاس رو به کلاس پدرش یا سوپر کلاس متصل کنه و دسترسی بده از ما
"""
یک شی موقت از کلاس پدر یا کلاس پایه میسازه که ما با استفاده از اون میتونیم به اعضای اون کلاس پدر دسترسی داشته باشیم
"""


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

    def __init__(self, username: str, email: str, password: str) -> None:
        self.username = username
        self.email = email
        self.password = password
        User.all_users.append(self)

    def __str__(self):
        return f"{self.username} - {self.email} - {self.password}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.username!r}, {self.email!r}, {self.password!r})"


class Seller(User):
    def order(self, order: "Order") -> None:
        print(f"{self.username}, From your products, {order} was sold!")


class Buyer(User):
    def __init__(self, username: str, email: str, password: str, phone: str) -> None:
        super(Buyer, self).__init__(username, email, password)
        self.phone = phone

    def __str__(self):
        return f"{self.username} - {self.email} - {self.password} - {self.phone}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.username!r}, {self.email!r}, {self.password!r}, {self.phone!r})"


def main():
    buyer_account = Buyer(username='danial', email='danial@gmail.com', password='1234', phone='09391234567')
    # print(buyer_account)
    # print(repr(buyer_account))
    # ----------------------------
    # li = UserList()
    # li.append(buyer_account)
    # print(li)
    # ----------------------------
    print(User.all_users)


if __name__ == "__main__":
    main()

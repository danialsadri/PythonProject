# instance attribute ==> اتربیوتی هست که اختصاص داره به اون ابجکت و هر مقداری بگیره فقط توی اون ابجکتم میگیره
# class attribute ==> بین همه ابجکت ها و اینتنس ها این اتریبیوت باید مشترک باشه

class User:
    all_users: list["User"] = []

    def __init__(self, username: str, email: str, password: str) -> None:
        self.username = username
        self.email = email
        self.password = password
        User.all_users.append(self)

    def __str__(self):
        return f"{self.username} - {self.email} - {self.password}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.username!r}, {self.email!r}, {self.password!r})"


user_1 = User(username="hossein", email="hossein@email.com", password='1234')
# user_1.all_users = []
# User.all_users = []
user_2 = User(username="hasan", email="hasan@email.com", password='1234')

# print(str(user_1))
# print(repr(user_1))
# print(user_1.all_users)
print(User.all_users)

from pprint import pprint


class UserList(list["User"]):
    def search(self, username: str) -> list["User"]:
        matching_users: list["User"] = []
        for user in self:
            if username in user.username:
                matching_users.append(user)
        return matching_users


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


def main():
    user_1 = User(username="hasan", email="hossein@email.com", password='1234')
    user_2 = User(username="hasan01", email="hasan@email.com", password='1234')
    user_3 = User(username="akbar", email="akbar@email.com", password='1234')
    user_4 = User(username="akbar01", email="asghar@email.com", password='1234')
    # User.all_users.append('a')
    # print(User.all_users)
    pprint(User.all_users.search("akbar"))


if __name__ == "__main__":
    main()

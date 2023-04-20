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


class Seller(User):
    def order(self, order: "Order") -> None:
        print(f"{self.username}, From your products, {order} was sold!")


def main():
    user_1 = User(username="hossein", email="hossein@email.com", password='1234')
    seller_1 = Seller(username="hasan", email="hasan@email.com", password='1234')
    # seller_1.all_users = []
    seller_2 = Seller(username="akbar", email="akbar@email.com", password='1234')
    # print(f"{user_1.username} - {user_1.email} - {user_1.password}")
    # print(f"{seller_1.username} - {seller_1.email} - {seller_1.password}")
    # print(f"{seller_2.username} - {seller_2.email} - {seller_2.password}")
    # seller_1.order('book')
    print(seller_1.all_users)


if __name__ == "__main__":
    main()

from typing import List


class BankAccount:
    """
    Bank account management.
    """
    all_account_numbers: List[int] = []
    last_account_number = 999

    def __init__(self, name: str) -> None:
        BankAccount.last_account_number += 1
        an = BankAccount.last_account_number
        self.account_number: int = an
        BankAccount.all_account_numbers.append(an)
        self.name: str = name
        self.balance: float = 0

    def display(self) -> None:
        """
        Show account balance.
        """
        print('-' * 40)
        print(f"Hi, {self.name}\nYour current balance: {self.balance}")
        print('-' * 40)

    def deposit(self) -> None:
        """
        Increase account balance.
        """
        amount = float(input('Please enter amount to deposit:  '))
        self.balance += amount
        self.display()

    def withdraw(self) -> None:
        """
        withdraw from bank account.
        """
        amount = float(input('Please enter amount to withdraw: '))
        if amount > self.balance:
            print('Insufficient balance')
        else:
            self.balance -= amount
        self.display()


def main():
    account_1 = BankAccount('danial sadri')
    print('*' * 40)
    print(f"account_number: {account_1.account_number}")
    print('*' * 40)
    account_1.display()

    while True:
        choice = int(input('Enter:\n1 to see your balance\n2 to deposit\n3 to withdraw\n4 to exit\n\t\tyour choice: '))
        if choice == 1:
            account_1.display()
        elif choice == 2:
            account_1.deposit()
        elif choice == 3:
            account_1.withdraw()
        elif choice == 4:
            break
        else:
            print('Please enter a valid number.')


if __name__ == "__main__":
    main()

from typing import Union


class Account:
    def __init__(self, account_id: str, name: str, balance: int = 0):
        self.id = account_id  # .id is the name of attribute that attached to self has to match task description for Judge purposes
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount: int) -> Union[int, str]:
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self) -> str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"

a = Account(4, "Johnny", 9)
print(a.info())

account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())
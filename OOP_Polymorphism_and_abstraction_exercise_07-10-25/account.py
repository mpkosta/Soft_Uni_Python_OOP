class Account:
    def __init__(self, owner: str, amount: int=0):
        self.owner = owner
        self.amount = amount
        self._transactions: list = []

    @property #shortcut to the balance for the other 2 methods
    def balance(self):
        return sum(self._transactions) + self.amount

    def handle_transaction(self, transaction_amount: int):
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def add_transaction(self, amount: int):
        if not isinstance(amount, int): #if amount is not an integer
            raise ValueError("please use int for amount")
        return self.handle_transaction(amount)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        return iter(self._transactions)

    def __getitem__(self, index): #same as above __iter__ method
        return self._transactions[index]

    def __reversed__(self):
        return reversed(self._transactions)

    def __eq__(self, other):
        return self.balance == other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        new_owner = f"{self.owner}&{other.owner}"
        new_amount = self.amount + other.amount
        new_account = Account(new_owner, new_amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account


acc = Account('bob', 10)

acc2 = Account('john')

print(acc)

print(repr(acc))

acc.add_transaction(20)

acc.add_transaction(-20)

acc.add_transaction(30)

print(acc.balance)

print(len(acc))

for transaction in acc:
    print(transaction)

print(acc[1])

print(list(reversed(acc)))

acc2.add_transaction(10)

acc2.add_transaction(60)

print(acc > acc2)

print(acc >= acc2)

print(acc < acc2)

print(acc <= acc2)

print(acc == acc2)

print(acc != acc2)

acc3 = acc + acc2

print(acc3)

print(acc3._transactions)
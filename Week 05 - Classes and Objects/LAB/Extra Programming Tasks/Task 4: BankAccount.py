"""
## Task 4: Bank Account

Create a class `BankAccount` with `owner` and `balance` (default 0) and methods:
- `deposit(amount)`
- `withdraw(amount)` – refuse the withdrawal and print a message if there is not enough money
- `show_balance()`

Test it with several deposits and withdrawals, including one that should fail.
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += amount
        return print(f"You have deposited {amount}, your new balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"You do not have enough money to withdraw {amount}")
        else:
            self.balance -= amount
            print(f"Your new balance is {self.balance}")

    def show_balance(self):
        return print(f"Your balance is {self.show_balance}")

account = BankAccount("Abisola", 100)
print(account.show_balance())
print(account.deposit(300))
print(account.show_balance())
print(account.withdraw(250))
print(account.show_balance())
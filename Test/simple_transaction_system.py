# What a transaction engine means.abs
#
# In a blockchain context a transaction engine is a system that accepts transactions, validates them and updates them safely. So lets build that first

# First Goals:
# 1. Make Transactions.
# 2. Validate that they were successful (enough money)
# 3. Update the balances

from dataclasses import dataclass

@dataclass(slots=True)
class Account:
    username: str
    balance: int
    transactions: dict

    def check_balance(self):
        return self.balance

    def subtract_balance(self, amount):
        self.balance -= amount

    def add_to_balance(self, amount):
        self.balance += amount

    def create_transaction(self, recipient, amount):
        if amount < 0:
            return "FAILED. AMOUNT MUST BE GREATER THAN 0"

        # Check user has enough money
        balance = self.check_balance()

        if balance > amount:
            if recipient.process_transaction(self.username, amount):
                self.subtract_balance(amount)

    def process_transaction(self, sender, amount):
        if sender != self.username:
            if amount > 0:
                self.add_to_balance(amount)
                self.transactions[sender] = amount
                return True
            else:
                return False


alice = Account("Alice", 100, {})
bob = Account("Bob", 50, {})

alice.create_transaction(bob, 60)

print(alice.balance)
print(bob.balance)

print(bob.transactions)


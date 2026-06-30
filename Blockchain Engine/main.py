# What a transaction engine means.abs
#
# In a blockchain context a transaction engine is a system that accepts transactions, validates them and updates them safely. So lets build that first

# First Goals:
# 1. Make Transactions.
# 2. Validate that they were successful (enough money)
# 3. Update the balances

from dataclasses import dataclass
from datetime import datetime

@dataclass(slots=True, frozen=True)
class Transaction:
    id: str
    sender: str
    recipient: str
    amount: int
    time: datetime.datetime

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

@dataclass
class Blockchain:
    transactions: list[Transaction]
    transaction_id: int

    def process_transaction(self, sender, recipient, amount, validation_key) -> True | False:
        validation_keys = [1212, 5678, 9876]

        if validation_key in validation_keys:
            if sender.balance >= amount:
                self.create_transaction_log(Transaction(self.get_transaction_id(), sender.username, recipient.username, amount, datetime.now()))
                sender.subtract_balance(amount)
                recipient.add_to_balance(amount)

                return True
            
        return False

    def get_transaction_id(self):
        self.transaction_id += 1
        return self.transaction_id

    def view_transaction_log(self):
        print(self.transactions)

    def create_transaction_log(self, transaction):
        self.transactions.append(transaction)

def user_create_transaction(sender_object, recipient_object, amount, validation_key, blockchain):
    if blockchain.process_transaction(sender_object, recipient_object, amount, validation_key):
        return "Transaction Successful"
    return "Transaction Failed"
    
blockchain = Blockchain([], 0)

alice = Account("Alice", 100, {})
bob = Account("Bob", 50, {})

print(user_create_transaction(alice, bob, 60, 1212, blockchain))

print(alice.balance)
print(bob.balance)

print(blockchain.view_transaction_log())

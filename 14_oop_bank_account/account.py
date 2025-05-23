class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float):
        if amount <= 0: raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0: raise ValueError("Amount must be positive")
        if amount > self.balance: raise ValueError("Insufficient funds")
        self.balance -= amount

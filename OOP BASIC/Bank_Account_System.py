class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"{amount}rs deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"{amount}rs withdrawn successfully.")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")

account = BankAccount("Satyam", 1000)

account.deposit(500)
account.withdraw(300)
account.display_balance()

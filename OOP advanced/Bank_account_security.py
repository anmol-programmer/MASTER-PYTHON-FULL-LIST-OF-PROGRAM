def info():
    """
    Problem:
Create a BankAccount class:

private variable __balance

methods: deposit(), withdraw()

direct balance access not allowed

📌 Job Use: Secure financial systems
    """
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance   # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def get_balance(self):
        """Read-only access to balance"""
        return self.__balance
account = BankAccount("Satyam", 5000)

account.deposit(2000)
account.withdraw(3000)

print("Current Balance:", account.get_balance())

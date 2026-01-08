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
        return self.__balance



name = input("Enter account holder name: ")
balance = int(input("Enter initial balance: "))

account = BankAccount(name, balance)

while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = int(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        print("Current Balance: ₹", account.get_balance())

    elif choice == "4":
        print("Thank you for using the bank system 🙏")
        break

    else:
        print("Invalid choice! Try again.")

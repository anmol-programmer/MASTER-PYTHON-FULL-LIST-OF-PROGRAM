class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self.__balance += amount
            print("Amount deposited successfully")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Amount withdrawn successfully")

    def get_balance(self):
        print("Current balance is", self.__balance)
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, balance)

while True:
    print("\nBank Menu")
    print("1 Deposit")
    print("2 Withdraw")
    print("3 Check Balance")
    print("4 Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        case "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        case "3":
            account.get_balance()

        case "4":
            print("Thank you for using the banking system")
            break

        case _:
            print("Invalid choice")

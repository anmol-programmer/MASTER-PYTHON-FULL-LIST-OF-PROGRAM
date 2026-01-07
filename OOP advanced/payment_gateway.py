

class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"{amount} rs paid successfully using UPI")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"{amount} rs paid successfully using Card")

class NetBankingPayment(Payment):
    def pay(self, amount):
        print(f"{amount} rs paid successfully using Net Banking")
def info_program():
    """
    Problem:
    Create a Payment class with method pay(amount)
    Create subclasses:
    UPIPayment
    CardPayment
    NetBankingPayment

    Job Use: E-commerce checkout systems
    """
    print("This program demonstrates polymorphism in a payment system.")

print("Press 1 to know about the program")
print("Press 2 for UPI Payment")
print("Press 3 for Card Payment")
print("Press 4 for Net Banking Payment")

n = int(input("Enter your choice: "))

match n:
    case 1:
        print(info_program.__doc__)

    case 2:
        user_amount = int(input("Enter the amount: "))
        payment = UPIPayment()
        payment.pay(user_amount)

    case 3:
        user_amount = int(input("Enter the amount: "))
        payment = CardPayment()
        payment.pay(user_amount)

    case 4:
        user_amount = int(input("Enter the amount: "))
        payment = NetBankingPayment()
        payment.pay(user_amount)

    case _:
        print("Enter a valid choice.")


        
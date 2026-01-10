class CardPayment:
    def pay(self, amount):
        print("Card payment completed")
        print("Paid amount", amount)

class UPIPayment:
    def pay(self, amount):
        print("UPI payment completed")
        print("Paid amount", amount)

class CashOnDelivery:
    def pay(self, amount):
        print("Cash on Delivery selected")
        print("Payable amount", amount)
class User:
    def set_user(self, name):
        self.name = name

    def show_user(self):
        print("User name", self.name)

class Customer(User):
    def set_customer(self, address):
        self.address = address

    def show_customer(self):
        self.show_user()
        print("Delivery address", self.address)
class Order:
    def create_order(self, order_id, customer, amount):
        self.order_id = order_id
        self.customer = customer
        self.__amount = amount
        self.__status = "Created"

    def get_amount(self):
        return self.__amount

    def confirm_order(self):
        self.__status = "Confirmed"

    def cancel_order(self):
        self.__status = "Cancelled"

    def get_status(self):
        return self.__status
class OrderService:
    def process_order(self, order, payment):
        print("\nProcessing order")
        print("Order ID", order.order_id)
        order.customer.show_customer()

        payment.pay(order.get_amount())

        order.confirm_order()
        print("Order status", order.get_status())
customer = Customer()
customer.set_user(input("Enter customer name: "))
customer.set_customer(input("Enter delivery address: "))

amount = float(input("Enter order amount: "))

order = Order()
order.create_order(101, customer, amount)

print("\nSelect payment method")
print("1 Card")
print("2 UPI")
print("3 Cash on Delivery")

choice = input("Enter choice: ")

if choice == "1":
    payment = CardPayment()
elif choice == "2":
    payment = UPIPayment()
elif choice =="3":
    payment = CashOnDelivery()

service = OrderService()
service.process_order(order, payment)


def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount

try:
    current_balance = 5000
    withdraw_amount = int(input("Enter amount to withdraw: "))

    remaining_balance = withdraw(current_balance, withdraw_amount)
    print("Remaining balance:", remaining_balance)

except ValueError as e:
    print(e)

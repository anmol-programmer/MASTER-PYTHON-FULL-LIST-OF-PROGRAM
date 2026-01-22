class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    try:
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        if amount > balance:
            raise InsufficientBalanceError("Insufficient balance")

        balance -= amount

    except (TypeError, ValueError) as e:
        print("Input Error:", e)

    except InsufficientBalanceError as e:
        print("Transaction Error:", e)

    else:
        print("Withdrawal successful")
        print("Remaining balance:", balance)

    finally:
        print("Transaction completed")

    return balance


balance = withdraw(5000, 1500)

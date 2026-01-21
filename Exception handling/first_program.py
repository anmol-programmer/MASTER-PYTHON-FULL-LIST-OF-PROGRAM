try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Please enter valid integer numbers only.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Division performed successfully.")

finally:
    print("Program execution completed.")

# Custom Exception
class InsufficientBalanceError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# Function to withdraw money
def withdraw(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError("Insufficient Balance!")

    balance -= amount
    return balance


# Main Program
try:

    # Input from user
    balance = float(input("Enter your account balance: "))
    amount = float(input("Enter withdrawal amount: "))

    # Calling function
    new_balance = withdraw(balance, amount)

except ValueError:
    print("Error: Please enter numeric values.")

except ZeroDivisionError:
    print("Error: Division by zero occurred.")

except InsufficientBalanceError as e:
    print("Custom Exception:", e)

else:
    print("Transaction successful.")
    print("Remaining Balance:", new_balance)

finally:
    print("Thank you for using the banking system.")
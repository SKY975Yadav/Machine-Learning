# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("Invalid input! Please enter a number.")
    
    
# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# else:
#     print("Division succeeded:", result)

# try:
#     file = open("sample.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     file.close()
#     print("File closed.")

# try:
#     result = 10 / "a"  # This will raise a TypeError
# except Exception as e:
#     print(f"An error occurred: {e}")

try:
    number = int(input("Enter a positive number: "))
    if number < 0:
        raise ValueError("Number must be positive.")
except ValueError as e:
    print(e)


class InsufficientFundsError(Exception):
    """Raised when an attempt is made to withdraw more funds than available."""
    pass

def withdraw_funds(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Insufficient funds for this withdrawal.")
    balance -= amount
    return balance

# Example usage
try:
    balance = 100
    amount = 150
    balance = withdraw_funds(balance, amount)
except InsufficientFundsError as e:
    print(e)

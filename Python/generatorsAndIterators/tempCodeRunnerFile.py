
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

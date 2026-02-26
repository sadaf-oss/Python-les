print("Simple Calculator Program")
print("Welcome to my calculator")

# User se input leana
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

# Calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Division ke liye check (0 se divide na ho)
if num1 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

print("\nResults:") 
print("Addition:", addition) 
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division) 

print("\nThank you for using this program")
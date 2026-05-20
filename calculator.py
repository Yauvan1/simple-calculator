# =====================================
# Simple Calculator in Python
# =====================================

print("Simple Calculator")

# First number
num1 = float(input("Enter first number: "))

# Operator
operator = input("Enter operator (+, -, *, /): ")

# Second number
num2 = float(input("Enter second number: "))

# Calculations
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Cannot divide by zero."

else:
    result = "Invalid operator."

# Show result
print("Result:", result)

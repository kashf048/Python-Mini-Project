# PYTHON CALCULATOR

# Ask the user to enter an operator (+, -, /, *).
# Ask the user to enter the first number.
# Ask the user to enter the second number.
# Check the operator:
# If operator is +:
# Add the two numbers and print the result.
# If operator is -:
# Subtract the second number from the first and print the result.
# If operator is /:
# Divide the first number by the second and print the result.
# If operator is *:
# Multiply the two numbers and print the result.
# Otherwise:
# Print "Invalid operator."

operator = input('Enter an operator ( + - / * ): ')
num1 = float(input('Enter the 1st number: '))
num2 = float(input('Enter the 2st number: '))

if operator == '+':
    result = num1 + num2
    print(round(result, 3))
elif operator == '-':
    result = num1 - num2
    print(round(result, 3))
elif operator == '/':
    result = num1 / num2
    print(round(result, 3))
elif operator == '*':
    result = num1 * num2
    print(round(result, 3))
else:
    print(f"{operator} is not valid operator")
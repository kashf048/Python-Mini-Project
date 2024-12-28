# Python credit card validator program DIFFICULT

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd paces from right to left
# 3. Double every second digit from right to left.
#       (If result is a two-digit number,
#       add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

# Example: 378282246310005, 6011111111111117, 5555555555554444

# Initialize:

# Set sum_odd_digits, sum_even_digits, and total to 0.
# Input:

# Ask the user to enter a credit card number.
# Remove all spaces and dashes from the input.
# Reverse the card number for processing.
# Process Odd-Position Digits:

# Loop through every second digit starting from the first (odd positions in reversed number).
# Add each digit directly to sum_odd_digits.
# Process Even-Position Digits:

# Loop through every second digit starting from the second (even positions in reversed number).
# Multiply each digit by 2.
# If the result is greater than or equal to 10:
# Add 1 + (result % 10) to sum_odd_digits.
# Else:
# Add the result to sum_even_digits.
# Calculate Total:

# Add sum_odd_digits and sum_even_digits.
# Validate:

# If total % 10 == 0:
# Print "VALID".
# Else:
# Print "INVALID".


sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1
card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

# Step 2
for x in card_number[::2]:
    sum_odd_digits += int(x)

# Step 3
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_odd_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# Step 4
total = sum_even_digits + sum_odd_digits

# Step 5
if total % 10 == 0:
    print('VALID')
else:
    print('INVALID')
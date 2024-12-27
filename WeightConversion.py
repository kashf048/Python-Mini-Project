# Python weight converter

# Ask the user for their weight.
# Ask if the weight is in kilograms (K) or pounds (L).
# Convert input to uppercase.
# If the unit is K:
# Convert weight to pounds (weight×2.205\text{weight} \times 2.205weight×2.205).
# Print the result in pounds.
# If the unit is L:
# Convert weight to kilograms (weight÷2.205\text{weight} \div 2.205weight÷2.205).
# Print the result in kilograms.
# Otherwise:
# Print "Invalid input."

weight = float(input('Enter your weight: '))
unit = input('Kilograms or Pounds? (K or L): ').upper()

if unit == 'K':
    weight = weight * 2.205
    unit = 'Lbs.'
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == 'L':
    weight = weight / 2.205
    unit = 'Kgs.'
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f'{unit} was no valid')
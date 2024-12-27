# Temperature Conversion

# Ask the user if the temperature is in Celsius (C) or Fahrenheit (F).
# Convert the input to uppercase.
# Ask the user to enter the temperature value.
# Check the unit:
# If unit is C:
# Convert to Fahrenheit using: F=95×C+32\text{F} = \frac{9}{5} \times \text{C} + 32F=59​×C+32.
# Print the result.
# If unit is F:
# Convert to Celsius using: C=59×(F−32)\text{C} = \frac{5}{9} \times (\text{F} - 32)C=95​×(F−32).
# Print the result.
# Otherwise:
# Print "Invalid unit."



unit = input('Is the temperature is Celcius or Fahrenheit (C/F): ').upper()
temp = float(input('Enter the temperature: '))

if unit == 'C':
    temp = round((9 * temp) / 5 + 32, 1)
    print(f'The temperature is Fahrenheit is: {temp}°')
elif unit == 'F':
    temp = round((temp - 32) * 5 / 9, 1)
    print(f'The temperature is Celcius is: {temp}°')
else:
    print(f'{unit} is an invalid unit of measurement')
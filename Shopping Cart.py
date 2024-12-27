# Shopping Cart Program

# Initialize an empty list for foods and prices.

# Set total to 0.

# Repeat:

# Ask the user to enter a food item or type q to quit.
# If the user enters q:
# Exit the loop.
# Otherwise:
# Ask for the price of the food.
# Add the food to the foods list.
# Add the price to the prices list.
# Print "----- YOUR CART -----".

# For each food in the foods list:

# Print the food.
# For each price in the prices list:

# Add the price to the total.
# Print the total cost.

foods = []
prices = []
total = 0

while True:
    food = input('Enter a food to buy (q to quit): ')
    if food.lower() == 'q':
        break
    else:
        price = float(input(f'Enter the price of a {food}: $'))
        foods.append(food)
        prices.append(price)

print('----- YOUR CART -----')

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f'Your total is: ${total}')
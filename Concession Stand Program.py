# Concession stand program

# Initialize:
# A dictionary containing food items and their prices.
# An empty list to store the items in the cart.
# Set total to 0.
# Display Menu:
# Print each food item and its price from the menu.
# Repeat:
# Ask the user to select a food item or type q to quit.
# If the user enters q:
# Exit the loop.
# If the food exists in the menu:
# Add the food to the cart.
# Print Order Summary:
# Display all items in the cart.
# Add the price of each item to the total.
# Print the total cost.

menu = {"pizza": 3.00,
        "popcorn": 6.00,
        "fries": 2.60,
        "chips": 1.00,
        "soda": 3.00,
        "lamonade": 4.25,
        "sandwich": 4.50,
        "coffee":1.25}

cart = []
total = 0

print('---------- MENU ----------')
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print('--------------------------')

while True:
    food = input('Select an item (q to quit): ').lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
    
print("-------- YOUR ORDER --------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")
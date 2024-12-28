# Dice Roller Program

# Initialize:

# Create a dictionary to store dice art for numbers 1 to 6.
# Initialize an empty list for rolled dice.
# Set total to 0.
# Input:

# Ask the user how many dice they want to roll.
# Roll Dice:

# For the number of dice specified by the user:
# Generate a random number between 1 and 6 for each die.
# Add the number to the dice list.
# Display Dice Art Horizontally:

# Loop through each line of the dice art (0 to 4).
# For each die, print the corresponding line from the dice art dictionary.
# Print all dice art on the same line, then move to the next.
# Calculate Total:

# Loop through the rolled dice list.
# Add each die value to the total.
# Output:

# Print the total of all rolled dice.

import random

# print("\u25CF, \u250C, \u2500, \u2510, \u2502, \u2514, \u2518")
# ●, ┌, ─, ┐, │, └, ┘
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),
    2: ("┌─────────┐", 
        "│ ●       │", 
        "│         │", 
        "│       ● │", 
        "└─────────┘"),
    3: ("┌─────────┐", 
        "│ ●       │", 
        "│    ●    │", 
        "│       ● │", 
        "└─────────┘"),
    4: ("┌─────────┐", 
        "│ ●     ● │", 
        "│         │", 
        "│ ●     ● │", 
        "└─────────┘"),
    5: ("┌─────────┐", 
        "│ ●     ● │", 
        "│    ●    │", 
        "│ ●     ● │", 
        "└─────────┘"),
    6: ("┌─────────┐", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# Vertical
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

# Horizantal
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"total: {total}")
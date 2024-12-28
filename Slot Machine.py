# Slot Machine

# Define Function: spin_row()

# Create a list of symbols: 🍒, 🍉, 🍋, 🔔, ⭐.
# Randomly select three symbols.
# Return the three selected symbols as a list.
# Define Function: print_row(row)

# Print the row with the symbols separated by |.
# Define Function: get_payout(row, bet)

# If all three symbols in the row are the same:
# If symbol is:
# 🍒 → Return bet * 3.
# 🍉 → Return bet * 4.
# 🍋 → Return bet * 5.
# 🔔 → Return bet * 10.
# ⭐ → Return bet * 20.
# Else:
# Return 0.
# Define Main Function: main()

# Set the initial balance to $100.

# Display a welcome message and the available symbols.

# While balance is greater than 0:

# Display the current balance.
# Ask the user to place a bet.
# If bet is not valid (not a number, less than 1, or more than the balance):
# Show an error message and restart the loop.
# Subtract the bet from the balance.
# Spin the slot machine (spin_row()) and print the result (print_row(row)).
# Calculate the payout using get_payout(row, bet).
# If payout > 0:
# Add payout to the balance.
# Show the winning message.
# Else:
# Show the losing message.
# Ask the user if they want to play again.
# If user chooses not to play again:
# Exit the loop.
# Display the game-over message with the final balance.

# Run Program:

# Call main() to start the program.

import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]

    # result = []
    # for symbol in range(3):
    #     result.append(random.choice(symbols))
    # return result

def print_row(row):
    print("****************")
    print(" | ".join(row))
    print("****************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100

    print("*************************")
    print("Welcome to Python Slots ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    while balance > 0:
        print(f"Current balcance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            break

    print("*******************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("*******************************************")

if __name__ == '__main__':
    main()
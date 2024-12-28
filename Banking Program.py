# Python Banking Program

# Define Function: show_balance(balance)

# Display the current balance.
# Define Function: deposit()

# Ask the user for the deposit amount.
# If the amount is less than 0:
# Show an error message.
# Return 0.
# Else:
# Return the deposit amount.
# Define Function: withdraw(balance)

# Ask the user for the withdrawal amount.
# If the amount is greater than the balance:
# Show an insufficient balance message.
# Return 0.
# Else If the amount is less than 0:
# Show an error message.
# Return 0.
# Else:
# Return the withdrawal amount.
# Define Main Function: main()

# Set the initial balance to 0.
# Set is_running to True.
# While is_running:
# Display the menu:
# Show Balance.
# Deposit.
# Withdraw.
# Exit.
# Ask the user for their choice.
# If choice is 1:
# Call show_balance(balance).
# Else If choice is 2:
# Add the result of deposit() to the balance.
# Else If choice is 3:
# Subtract the result of withdraw(balance) from the balance.
# Else If choice is 4:
# Set is_running to False.
# Else:
# Show an invalid choice message.
# End:

# Display a thank-you message.
# Run Program:

# Call main() to start the program.

def show_balance(balance):
    print("*********************")
    print(f"Your balance is ${balance:.2f}")
    print("*********************")

def deposit():
    print("*********************")
    amount = float(input("Enter an amount to be deposit: "))
    print("*********************")

    if amount < 0:
        print("*********************")
        print("That's not a valid amount")
        print("*********************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("*********************")
    amount = float(input("Enter amount to be withdraw: "))
    print("*********************")

    if amount > balance:
        print("*********************")
        print("Insufficient balance")
        print("*********************")
        return 0
    elif amount < 0:
        print("*********************")
        print("Amount must be greater than 0")
        print("*********************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print("   Banking Program   ")
        print("*********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")

        choice = input("Enter your choice(1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*********************")
            print('That is not a valid choice!')
            print("*********************")

    print("*********************")
    print("Thank You! Have a nice day")
    print("*********************")

if __name__ == '__main__':
    main()
# Number guessing game

# Initialize:

# Set the range of numbers (lowest and highest).
# Generate a random number as the answer.
# Set the number of guesses to 0.
# Set a flag (is_running) to True.
# Display Instructions:

# Inform the user about the range of numbers to guess from.
# Repeat While Game is Running:

# Ask the user to input a guess.
# If the guess is a valid number:
# Convert the guess to an integer.
# Increment the number of guesses.
# If the guess is out of range:
# Inform the user the guess is invalid and remind them of the range.
# If the guess is less than the answer:
# Print "Too low! Try Again!".
# If the guess is greater than the answer:
# Print "Too high! Try Again!".
# If the guess is equal to the answer:
# Print "CORRECT!" and the number of guesses.
# Set is_running to False to end the game.
# Else:
# Inform the user the input is invalid and remind them of the range.
# End of Game:

# Exit the loop when the correct number is guessed.

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print('Python Number Guessing Game')
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("The number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try Again!")
        elif guess > answer:
            print("Too high! Try Again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else:
        print('Invalid guess')
        print(f"Please select a number between {lowest_num} and {highest_num}")
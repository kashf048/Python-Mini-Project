# Hangman Game

# Import Modules

# Import the word list and the random module.
# Define Hangman Art

# Create a dictionary hangman_art for different stages of the hangman drawing (from empty to fully drawn).
# Define Function: display_man(wrong_guesses)

# Display the hangman art based on the number of wrong guesses.
# Define Function: display_hint(hint)

# Print the current hint with spaces between letters.
# Define Function: display_answer(answer)

# Print the complete answer.
# Define Main Function: main()

# Select a random word from the word list.

# Create a hint list with underscores _ for each letter in the word.

# Initialize wrong_guesses to 1.

# Create a guessed_letters set to track guessed letters.

# Set is_running to True.

# While is_running is True:

# Display the current hangman art (display_man(wrong_guesses)).
# Display the current hint (display_hint(hint)).
# Ask the user for a letter.
# If the input is invalid (not a single letter):
# Show an error message and restart the loop.
# If the letter is already guessed:
# Show a message and restart the loop.
# Add the guessed letter to guessed_letters.
# If the guessed letter is in the answer:
# Update the hint list at all matching positions.
# Else:
# Increment wrong_guesses.
# If all letters are guessed (no _ in the hint):
# Display the full hangman art and the answer.
# Show a "YOU WIN" message.
# Set is_running to False.
# If the maximum wrong guesses are reached:
# Display the full hangman art and the answer.
# Show a "YOU LOSE" message.
# Set is_running to False.
# Run Program

# Call main() to start the game.

from HangmanWordsList import words
import random

hangman_art = { 0: ("   ", 
                    "   ", 
                    "   "),
                1: (" O ", 
                    "   ", 
                    "   "),
                2: (" O ", 
                    " | ", 
                    "   "),
                3: (" O ", 
                    "/| ", 
                    "   "),
                4: (" O ", 
                    "/|\\", 
                    "   "),
                5: (" O ", 
                    "/|\\", 
                    "/  "),
                6: (" O ", 
                    "/|\\", 
                    "/ \\"),
                    }

# print(hangman_art[1])
# for line in hangman_art[5]:
#     print(line)

def display_man(wrong_guesses):

    print('***************')
    for line in hangman_art[wrong_guesses]:
        print(line)
    print('***************')

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 1
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        # display_answer(answer)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            is_running = False
        elif wrong_guesses >= len(hangman_art)- 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__ == "__main__":
    main()
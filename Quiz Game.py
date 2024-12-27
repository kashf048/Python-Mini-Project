# Quiz Game

# Initialize:
# A list of questions.
# A list of options corresponding to each question.
# A list of correct answers.
# An empty list to store user guesses.
# Set the score to 0.
# Loop through each question:
# Display the question and its options.
# Ask the user to input their guess (A, B, C, or D).
# Add the guess to the list of guesses.
# If the guess is correct:
# Increase the score by 1.
# Print "CORRECT!".
# Otherwise:
# Print "INCORRECT!" and display the correct answer.
# After all questions:
# Print a "RESULT" header.
# Display the correct answers and the user's guesses.
# Calculate the score as a percentage:
# score=correct answerstotal questions×100\text{score} = \frac{\text{correct answers}}{\text{total questions}} \times 100score=total questionscorrect answers​×100.
# Print the user's final score.

questions = (("How many elements are in the periodic table?: "), 
             ("Which animal lays the largest eggs?: "), 
             ("What is the most abundant gas in Earth's atmosphere?: "), 
             ("How many bones are in the human body?: "), 
             ("Which planet in the solar system is the hottest?: "))

options = (("A. 116", "B. 117", "C. 118", "D. 119"), 
           ("A. Whale", "B. Elephant", "C. Crocdile", "D. Ostrich"), 
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dixode", "D. Hydrogen"), 
           ("A. 206", "B. 207", "C. 208", "D. 209"), 
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print('---------------------------')
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('CORRECT!')
    else:
        print('INCORRECT!')
        print(f'{answers[question_num]} is the correct answer')
    question_num += 1

print('---------------------------')
print('          RESULT           ')
print('---------------------------')

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f'Your score is: {score}%')
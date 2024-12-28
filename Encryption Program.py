# Encryption Program

# Initialize:

# Define chars as a list of all possible characters (space, punctuation, digits, and letters).
# Copy chars to key.
# Shuffle the key list randomly.
# Encrypt Message:

# Input: Ask the user to enter a message to encrypt.
# Initialize an empty string for cipher_text.
# For each letter in the input message:
# Find the index of the letter in chars.
# Use this index to find the corresponding letter in key.
# Append the letter from key to cipher_text.
# Display the original message and its encrypted version.
# Decrypt Message:

# Input: Ask the user to enter a message to decrypt.
# Initialize an empty string for plain_text.
# For each letter in the input message:
# Find the index of the letter in key.
# Use this index to find the corresponding letter in chars.
# Append the letter from chars to plain_text.
# Display the encrypted message and its original (decrypted) version.

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Orignal message: {plain_text}")
print(f"Encryption message: {cipher_text}")

# DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encryption message: {cipher_text}")
print(f"Orignal message: {plain_text}")
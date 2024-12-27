# Ask the user to enter their email address.
# Extract the part of the email before the @ symbol as the username.
# Extract the part of the email after the @ symbol as the domain.
# Print the username and domain.

email = input('Enter your email: ')

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f'Your username is {username} and domain is {domain}')
import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Characters to use in password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# User input
try:
    length = int(input("Enter desired password length: "))
    password = generate_password(length)
    print("Generated password:", password)
except ValueError:
    print("Please enter a valid number.")

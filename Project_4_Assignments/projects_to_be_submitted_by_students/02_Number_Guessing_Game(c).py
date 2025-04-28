import random

def computer_guess():
    print("Think of a number between 1 and 100, and I will try to guess it!")

    low = 1
    high = 100
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Only one number left to guess

        print(f"My guess is: {guess}")
        feedback = input("Is it too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Yay! I guessed your number: {guess}")
        else:
            print("Please enter H, L, or C only.")

# Run the game
computer_guess()

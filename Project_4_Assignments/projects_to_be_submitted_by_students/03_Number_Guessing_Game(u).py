import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100...")

    # Computer picks a random number between 1 and 100
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0

    # Game loop
    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()

